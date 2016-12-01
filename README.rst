*******************************************************************************
A Social wall with Django generic views and custom users based on AbstractUser.
*******************************************************************************

History
=======

This app was originally designed to achieve an online Django course. Playing with Django was fun and I'm curious, so I decided to explore it a little further.
The project is running on a VPS with Debian 7, Python 3, PostgreSQL and virtualenv, you can see a live demo here:

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

Preview
=======

.. image:: https://raw.githubusercontent.com/NicolasMura/social-wall/master/social/static/social/img/social-wall-demo.jpg
    :alt: Social Wall Preview
    :target: http://vps121400.ovh.net/

.. note:: This project is for self-practise purpose, any suggestion and / or improvment's idea is welcome !
