========================
djangocms-ckeditor-filer
========================

Deprecated
==========
This project has been deprecated in favour of [`django-ckeditor-filebrowser-filer`](https://github.com/nephila/django-ckeditor-filebrowser-filer) which is maintained by the same guys who do Django-CMS itself and works better with newer versions. Use that!

What
====

This is the bastard lovechild of ``djangocms-text-ckeditor`` and ``django-ckeditor-filer``. Use this in your DjangoCMS 3 project to insert and edit images in CKEditor using filer, **without** having to use DjangoCMS's plugin system.

Why
===

This has a couple of advantages:

1. Images in HTMLFields (i.e., in models outside the CMS)

   Because of the way DjangoCMS works, you can't insert plugins (e.g., an image) into models in your own apps without using a ``PlaceholderField``. Using PlaceholderFields has a couple of drawbacks, the main one being no back-end editing of objects. You can use an ``HTMLField`` which gives you the DjangoCMS CKEditor, but without the ability to insert plugins - so no way to insert images. Until now!

2. Consistant CKEditor experience throughout the your whole project

   If you don't use any other plugins in your text fields, it's possible to configure CKEditor to hide the 'CMS Plugins' drop-down, so all your text editors look and work the same -- on both ``HTMLFields`` CMS text plugins, and text 'inside' the CMS, e.g., in Placeholders.

How (to install)
================

This works 'on top' of ``djangocms-text-ckeditor``, so you'll need that installed. You'll also need the various modules of ``cmsplugin-filer`` installed and working.

1. Install the package into your Python environment as usual (e.g., python setup.py install)

2. Add ``djangocms_ckeditor_filer.middleware.ThumbnailMiddleware`` in your ``MIDDLEWARE_CLASSES`` (this is for dynamic thumbnail generation)

3. Add ``djangocms_ckeditor_filer`` to your ``INSTALLED_APPS``

4. In your ``CKEDITOR_SETTINGS``, add::

    'extraPlugins': 'filerimage',
    'removePlugins': 'image',

   somewhere into the main dict, and::

    'Filer Image'

   somewhere in the toolbar(s), to display the button. For example::

    CKEDITOR_SETTINGS = {
      'language': '',
      'skin': 'moono',
      'toolbar': 'HTMLField',
      'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['ShowBlocks'],
        ['Format', 'Styles'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        ['Link', 'Unlink'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table', 'Filer Image'],
        ['Source']
      ],
      'extraPlugins': 'filerimage',
      'removePlugins': 'image'
    }

   That should be it!

Who
===

This project wouldn't be possible without Divio's DjangoCMS, cmsplugin-filer by Stefan Foulis and django-ckeditor-filer by IKRESOFT.
