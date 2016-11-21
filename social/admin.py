# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _, ungettext

# from django_comments import get_model
from django_comments.views.moderation import (
    perform_flag,
    perform_approve, perform_delete
)

from .models import Profile, Post, Comment


def moderate_comments(modeladmin, request, queryset):
    """ Set is_removed à True to all selected entries."""
    queryset.update(is_removed=True)

moderate_comments.short_description = "Modérer (désactiver) "\
    "les commentaires sélectionnés"


def cancel_comments_moderation(modeladmin, request, queryset):
    """ Set is_removed à False to all selected entries."""
    queryset.update(is_removed=False)

cancel_comments_moderation.short_description = "Rétablir (activer) "\
    "les commentaires sélectionnés"


class ProfileAdmin(admin.ModelAdmin):
        list_display = ('username', )
        search_fields = ('username', 'email', )
        can_delete = False
        verbose_name_plural = 'Profils utilisateurs'


class CommentInline(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'submit_date',
        'wall',
        'preview',
        'is_public',
        'is_removed',
    )

    fieldsets = (
        (
            _('Content'),
            {'fields': ('author', 'content')}
        ),
        (
            _('Metadata'),
            {'fields': ('wall', 'is_public', 'is_removed')}
        ),
    )

    list_filter = ('submit_date', 'is_public', 'is_removed')
    date_hierarchy = 'submit_date'
    ordering = ('-submit_date',)
    # raw_id_fields = ('user',)
    search_fields = ('content', 'author', 'email')
    actions = ["approve_comments", "remove_comments"]

    inlines = [
        CommentInline
    ]

    def preview(self, post):
        if len(post.content) > 50:
            return "{}...".format(post.content[:50])

        return post.content

    preview.short_description = 'Aperçu du post'

    # Actions personnalisées
    actions = [moderate_comments, cancel_comments_moderation]

    def get_actions(self, request):
        actions = super(PostAdmin, self).get_actions(request)
        # Only superusers should be able to delete the comments from the DB.
        if not request.user.is_superuser and 'delete_selected' in actions:
            actions.pop('delete_selected')
        if not request.user.has_perm('django_comments.can_moderate'):
            if 'approve_comments' in actions:
                actions.pop('approve_comments')
            if 'remove_comments' in actions:
                actions.pop('remove_comments')
        return actions

    def flag_comments(self, request, queryset):
        self._bulk_flag(request, queryset, perform_flag,
                        lambda n: ungettext('flagged', 'flagged', n))

    flag_comments.short_description = _("Flag selected comments")

    def approve_comments(self, request, queryset):
        self._bulk_flag(request, queryset, perform_approve,
                        lambda n: ungettext('approved', 'approved', n))

    approve_comments.short_description = _("Approve selected comments")

    def remove_comments(self, request, queryset):
        self._bulk_flag(request, queryset, perform_delete,
                        lambda n: ungettext('removed', 'removed', n))

    remove_comments.short_description = _("Remove selected comments")

    def _bulk_flag(self, request, queryset, action, done_message):
        """
        Flag, approve, or remove some comments from an admin action. Actually
        calls the `action` argument to perform the heavy lifting.
        """
        n_comments = 0
        for comment in queryset:
            action(request, comment)
            n_comments += 1

        msg = ungettext('%(count)s comment was successfully %(action)s.',
                        '%(count)s comments were successfully %(action)s.',
                        n_comments)
        self.message_user(request, msg % {
            'count': n_comments,
            'action': done_message(n_comments),
            })


class CommentAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            _('Content'),
            # {'fields': ('user', 'user_name', 'user_email', 'comment')}
            {'fields': ('author', 'content')}
        ),
        (
            _('Metadata'),
            {'fields': ('related_post', 'is_public', 'is_removed')}
        ),
    )

    list_display = (
        'author',
        'submit_date',
        'preview',
        'is_public',
        'is_removed',
    )

    def preview(self, comment):
        if len(comment.content) > 50:
            return "{}...".format(comment.content[:50])

        return comment.content

    preview.short_description = 'Aperçu du commentaire'

    # Actions personnalisées
    actions = [moderate_comments, cancel_comments_moderation]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile, ProfileAdmin)
