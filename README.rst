*******************************************************************************
A Social wall with Django generic views and custom users based on AbstractUser.
*******************************************************************************

History
=======

This app was originally designed to achieve an online Django course. Playing with Django was fun and I'm curious, so I decided to explore it a little further.
The project is running on a VPS with Debian 7 and Python 3 installed. It currently fits with the following technical requirements: PostgreSQL, virtual environment (virtualenv), Nginx Web Server, Gunicorn HTTP server, Supervisor and of course Git.

You can see a live demo here:

* Live demo: http://vps121400.ovh.net/

Requirements
============

* `Django suit 0.2.22 <https://github.com/darklow/django-suit>`_
* `Django Suit <https://github.com/darklow/django-suit>`_
* `django-bootstrap3 <https://github.com/dyve/django-bootstrap3/blob/master/docs/quickstart.rst>`_
* `pillow <https://github.com/python-pillow/Pillow/tree/3.4.x>`_

If you don't use a virtual environment, you can easily install those modules on your machine using:

.. code-block:: shell

    pip install django-suit==0.2.22
    pip install pillow
    pip install django-bootstrap3

Setup
=====

.. code-block:: shell

    python3 manage.py migrate
    python3 manage.py createsuperuser
    python3 manage.py runserver


Documentation
=============

Note : there is no "friends" notion, which means that everybody can publish post and comments onto anybody's wall.

Improvments to come
===================

* Grosse faille de sécurité : un utilisateur peut accéder au profil d'un autre utilisateur... (get uniquement, ouf !)
* Update profile --> customiser le template + désactiver l'effacement de l'avatar + désactiver le lien de changement de mdp
* Simplifier la visualisation des utilisateurs dans l'admin (ex. potentiel à voir avec l'exo-2)
* Idée intéressante à creuser sur la correction OC (models.py) : class Meta: / ordering = ['-date']
* Idée intéressante à creuser sur la correction exo-2 (manage.py)
* Regarder https://github.com/django/django-contrib-comments/blob/master/django_comments/views/comments.py pour les posts et le remplissage des commentaires (??)
* Page 404
* Démo / Fake data
* Lazy Load
* Social login : https://simpleisbetterthancomplex.com/tutorial/2016/10/24/how-to-add-social-login-to-django.html
* Email process (process d'inscription au minimum)
* django_extensions
* Tests
* Ajax side-bar with current connected users (suivi du filtrage des administrateurs (seuls les utilisateurs normaux peuvent être visibles, cf. exo-2 avec un def get_queryset adapté)
* Langages management
* Profile saving with ajax modal (https://simpleisbetterthancomplex.com/tutorial/2016/11/15/how-to-implement-a-crud-using-ajax-and-json.html)
* Ajax upload redimensionning process during avatar upload (signin + updating profile)
* Reste à traduite quelques erreurs (cf. models.py)
* strip tags (cd. forms.py)

Preview
=======

.. image:: https://raw.githubusercontent.com/NicolasMura/social-wall/master/social/static/social/img/social-wall-demo.jpg
    :alt: Social Wall Preview
    :target: http://vps121400.ovh.net/

.. note:: This project is for self-practise purpose, any suggestion and / or improvment's idea is welcome !
