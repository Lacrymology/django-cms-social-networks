# -*- coding: utf-8 -*-

"""
.. module:: 
   :platform: Unix
   :synopsis: TODO

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms_social_networks import models

class TwitterSharePlugin(CMSPluginBase):
    """
    Google+ +1 button instance
    """
    module = "Twitter"
    model = models.TwitterShare
    name = "Twitter Share Plugin"
    render_template = 'cms_social_networks/twitter/share.html'

    def render(self, context, instance, placeholder):
        context.update({
            'twitshare': instance,
            'placeholder': placeholder
        })
        return context
plugin_pool.register_plugin(TwitterSharePlugin)
