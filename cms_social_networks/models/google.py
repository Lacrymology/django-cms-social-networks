# -*- coding: utf-8 -*-

"""
.. module:: 
   :platform: Unix
   :synopsis: TODO

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin

class GooglePlusOne(CMSPlugin):
    """
    Google+ +1 button plugin instance
    """
    SIZE_CHOICES = (
        ('small', _('small')),
        ('medium', _('medium')),
        ('standard', _('standard')),
        ('tall', _('tall')),
    )
    ANNOTATION_CHOICES = (
        ('none', _('none')),
        ('bubble', _('bubble')),
        ('inline', _('inline')),
    )
    ALIGN_CHOICES = (
        ('left', _('left')),
        ('right', _('right')),
    )
    EXPAND_CHOICES = (
        ('top', _('top')),
        ('right', _('right')),
        ('bottom', _('bottom')),
        ('left', _('left')),
    )
    url = models.CharField(max_length=256, blank=True,
        help_text=_("If left empty, it will default to rel=canonical and then "
                    "to document.location.href"))
    size = models.CharField(_('size'), max_length=10, choices=SIZE_CHOICES,
        default='standard')
    annotation = models.CharField(_('annotation'), max_length=10,
        choices=ANNOTATION_CHOICES, default='bubble',
        help_text=_("bubble: display the number of users that have +1'd the "
                    "page; inline: display profile pictures and count of users "
                    "who have +1'd the page"))
    width = models.SmallIntegerField(_('width'), blank=True, null=True,
        help_text=_("If annotation is set to 'inline', sets the width in "
                    "pixels to use for the button and its inline annotation. "
                    "If omitted, a button and its inline annotation use 450px. "
                    "See https://developers.google.com/+/web/+1button/#inline-annotation"))
    align = models.CharField(_("align"), max_length=10, choices=ALIGN_CHOICES,
        default="left")
    expandTo = models.CharField(_('expand to'), max_length=50,
        choices=EXPAND_CHOICES, blank=True, null=True,
        help_text="preferred position(s) to display hover and confirmation "
                  "bubbles")

    class Meta:
        app_label = 'cms_social_networks'
