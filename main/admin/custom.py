from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from reversion.admin import VersionAdmin

from ..models import CustomUser


class CustomAdminSite(AdminSite):
    site_url = None
    # Text to put at the end of each page's <title>.
    site_title = 'Сообщество Банка России'

    # Text to put in each page's <h1>.
    site_header = 'Сообщество Банка России'

    # Text to put at the top of the admin index page.
    index_title = 'Главная'


class VersionedUserAdmin(VersionAdmin, UserAdmin):
    fieldsets = (
        ('Персональная информация', {
            'fields': ('nickname', 'email', 'gender', 'city', 'birthday', 'type')
        }),
        ('Права', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Даты', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'nickname', 'full_name', 'type', 'gender', 'city', 'birthday',
                       'password1', 'password2'),
        }),
    )
    list_display = ('username', 'nickname', 'email', 'type', 'is_staff')
    list_filter = ('type',)
    search_fields = ('username', 'nickname', 'email')


class VersionedGroupAdmin(VersionAdmin, GroupAdmin):
    pass


admin_site = CustomAdminSite()

admin_site.register(CustomUser, VersionedUserAdmin)
admin_site.register(Group, VersionedGroupAdmin)
