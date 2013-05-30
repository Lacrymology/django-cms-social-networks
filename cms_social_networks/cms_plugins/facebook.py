from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms_social_networks import models

class FacebookCommentsPlugin(CMSPluginBase):
    module = "Facebook"
    model = models.FacebookComments
    name = 'Social Facebook Comments Plugin'
    render_template = 'cms_social_networks/facebook/comments.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance, 'name': self.name})
        return context

    def render(self, context, instance, placeholder):
        context.update({
            'comments': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(FacebookCommentsPlugin)

class FacebookFacepilePlugin(CMSPluginBase):
    module = "Facebook"
    model = models.FacebookFacepile
    name = 'Facebook Facepile Plugin'
    render_template = 'cms_social_networks/facebook/facepile.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance, 'name': self.name})
        return context

    def render(self, context, instance, placeholder):
        context.update({
            'facepile': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(FacebookFacepilePlugin)

class FacebookLikeboxPlugin(CMSPluginBase):
    module = "Facebook"
    model = models.FacebookLikebox
    name = 'Facebook Likebox Plugin'
    render_template = 'cms_social_networks/facebook/likebox.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance, 'name': self.name})
        return context

    def render(self, context, instance, placeholder):
        context.update({
            'likebox': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(FacebookLikeboxPlugin)

class FacebookLikePlugin(CMSPluginBase):
    module = "Facebook"
    model = models.FacebookLike
    name = 'Facebook Like Button Plugin'
    render_template = 'cms_social_networks/facebook/like.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance, 'name': self.name})
        return context

    def render(self, context, instance, placeholder):
        context.update({
            'like': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(FacebookLikePlugin)

class FacebookLoginButtonPlugin(CMSPluginBase):
    module = "Facebook"
    model = models.FacebookLoginButton
    name = 'Facebook Login Button Plugin'
    render_template = 'cms_social_networks/facebook/loginbutton.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance, 'name': self.name})
        return context

    def render(self, context, instance, placeholder):
        context.update({
            'loginbutton': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(FacebookLoginButtonPlugin)

class FacebookLivestreamPlugin(CMSPluginBase):
    module = "Facebook"
    model = models.FacebookLivestream
    name = 'Facebook Live stream Plugin'
    render_template = 'cms_social_networks/facebook/livestream.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance, 'name': self.name})
        return context

    def render(self, context, instance, placeholder):
        context.update({
            'livestream': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(FacebookLivestreamPlugin)


