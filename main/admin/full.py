from django.contrib.auth.models import Permission
from reversion.models import Revision, Version

from .custom import *


class FullAdminSite(AdminSite):
    site_url = None

    def has_permission(self, request):
        return request.user.is_superuser


full_admin_site = FullAdminSite(name='full')

full_admin_site.register(CustomUser, VersionedUserAdmin)
full_admin_site.register(Group, GroupAdmin)
full_admin_site.register(Permission)

full_admin_site.register(Revision)
full_admin_site.register(Version)
