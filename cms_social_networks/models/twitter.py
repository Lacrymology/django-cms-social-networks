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

class TwitterShare(CMSPlugin):
    TYPE_CHOICES = (
        ('twitter-share-button', _('share')),
        ('twitter-hashtag-button', _('hashtag')),
        ('twitter-mention-button', _('mention')),
    )
    COUNT_CHOICES = (
        ('none', _("don't show")),
        ('horizontal', _('horizontal')),
        ('vertical', _('vertical')),
    )
    SIZE_CHOICES = (
        ('medium', _('medium')),
        ('large', _('large')),
    )
    type = models.CharField(max_length=25, choices=TYPE_CHOICES, default='twitter-share-button')
    detail = models.CharField(max_length=140, blank=True, null=True, help_text=_("Fill in with the desired hashtag if type=hashtag or screen name if type=mention"))
    tweet_text = models.CharField(max_length=140, blank=True, null=True, help_text=_("Default twit text. Defaults to page title"))
    url = models.CharField(max_length=256, blank=True, null=True, help_text=_("If left empty, it will default to rel=canonical and then to document.location.href"))
    via = models.CharField(max_length=128, blank=True, null=True, help_text=_("Screen name of the user to attribute the tweet to"))
    related = models.CharField(max_length=256, blank=True, null=True, help_text=_('Accounts to suggest for following. Example: "anywhere:The Javascript API,sitestreams,twitter:The official account"'))
    count = models.CharField(max_length=15, choices=COUNT_CHOICES, default='horizontal', help_text=_('Count box position'))
    count_url = models.CharField(max_length=256, blank=True, null=True, help_text=_("URL to what your shared URL resolves. This is what will get counted. Defaults to `url`"))
    hashtags = models.CharField(max_length=140, blank=True, null=True, help_text=_("Comma-separated list of hashtags"))
    size = models.CharField(max_length=8, choices=SIZE_CHOICES, default='medium')
    # if false, data-dnt = true
    tailor = models.BooleanField(default=False, help_text=_("Tailored suggestions. More info at https://support.twitter.com/articles/20169421#"))

    def is_hashtag(self):
        return self.type == 'twitter-hashtag-button'

    def is_mention(self):
        return self.type == 'twitter-mention-button'

    class Meta:
        app_label = 'cms_social_networks'
