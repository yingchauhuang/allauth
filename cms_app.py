from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from menu import allauthMenu

class allauthApphook(CMSApp):
    name = _("allauthApphook")
    urls = ['allauth.urls']
    menu = [allauthMenu]

apphook_pool.register(allauthApphook)