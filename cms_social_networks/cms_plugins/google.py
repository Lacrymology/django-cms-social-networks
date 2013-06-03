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

class GooglePlusOnePlugin(CMSPluginBase):
    """
    Google+ +1 button instance
    """
    module = "Google+"
    model = models.GooglePlusOne
    name = "Google+ +1 Plugin"
    render_template = 'cms_social_networks/google/plus-one.html'

    def render(self, context, instance, placeholder):
        context.update({
            'plusone': instance,
            'placeholder': placeholder
        })
        return context
plugin_pool.register_plugin(GooglePlusOnePlugin)
