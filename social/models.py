# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.conf import settings
from django.db import models
# from django.contrib.sites.models import Site  # utile ?
# from django.utils.encoding import python_2_unicode_compatible  # utile ?


COMMENT_MAX_LENGTH = 1000


# @python_2_unicode_compatible
class PostCommentAbstract(models.Model):
    """
    A user post/comment about some object.
    """

    class Meta:
        abstract = True
        ordering = ('submit_date', )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Auteur'),
        blank=False,
        null=False,
        # related_name="%(class)s_comments",
        related_name="%(class)s_author",
        # on_delete=models.SET_NULL,
    )
    # Metadata about the post/comment
    submit_date = models.DateTimeField(
        verbose_name=_('Date de publication'),
        auto_now_add=True,
        auto_now=False,
    )
    is_public = models.BooleanField(
        verbose_name=_('publique ?'),
        default=True,
        help_text=_(
            'Uncheck this box to make the comment effectively '
            'disappear from the site.'
        ),
    )
    is_removed = models.BooleanField(
        verbose_name=_('Désactivé ?'),
        default=False,
        help_text=_(
            'Check this box if the comment is inappropriate. '
            'A "This comment has been removed" message will '
            'be displayed instead.'
        ),
    )

    # def get_absolute_url(self, anchor_pattern="#c%(id)s"):
    #     return self.get_content_object_url() + (
    #         anchor_pattern % self.__dict__)

    def get_as_text(self):
        """
        Return this comment as plain text. Useful for emails.
        """
        d = {
            'profile': self.profile,
            'date': self.submit_date,
            'comment': self.comment,
            'domain': self.site.domain,
        }
        return _(
            'Posted by %(profile)s '
            'at %(date)s\n\n%(comment)s\n\nhttp://%(domain)s'
        ) % d


class Post(PostCommentAbstract):
    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    wall = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Publié sur le mur de'),
        blank=False,
        null=False,
        # related_name="%(class)s_comments",
        related_name="wall",
    )
    content = models.TextField(
        verbose_name=_('Message'),
        max_length=COMMENT_MAX_LENGTH,
        default="",
        blank=False,
    )

    def __unicode__(self):
        return _("Post de %(author)s : %(content)s...") % {
            'author': self.author, 'content': self.content[:50]}


class Comment(PostCommentAbstract):
    class Meta:
        verbose_name = _('Commentaire')
        verbose_name_plural = _('Commentaires')

    related_post = models.ForeignKey(
        'social.Post',
        verbose_name=_('Post relatif'),
        blank=False,
        null=False,
        # related_name="%(class)s_comments",
        # on_delete=models.SET_NULL,
        # related_name="wall",
        )
    content = models.CharField(
        verbose_name=_('Commentaire'),
        max_length=COMMENT_MAX_LENGTH,
        default="",
        blank=False,
    )

    def __unicode__(self):
        return _("Commentaire de %(author)s : %(content)s...") % {
            'author': self.author, 'content': self.content[:50]}
