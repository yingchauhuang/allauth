from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class allauthMenu(CMSAttachMenu):
    name = _("allauth Menu") # give the menu a name, this is required.

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        nodes = []
        n = NavigationNode(_('signup'), "signup/", 1)
        n2 = NavigationNode(_('login'), "login/", 2)
        n3 = NavigationNode(_('password change'), "password/change/", 3)
        n4 = NavigationNode(_('password reset'), "password/reset/", 4)
        nodes.append(n)
        nodes.append(n2)
        nodes.append(n3)
        nodes.append(n4)
        return nodes
menu_pool.register_menu(allauthMenu) # register the menu.