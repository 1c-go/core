from django.apps import AppConfig
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class MainConfig(AppConfig):
    name = 'main'
    verbose_name = 'Основное'


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'

    '''
    menu = (
        ParentItem('Content', children=[
            ChildItem(model='demo.country'),
            ChildItem(model='demo.continent'),
            ChildItem(model='demo.showcase'),
            ChildItem('Custom view', url='/admin/custom/'),
        ], icon='fa fa-leaf'),
        ParentItem('Integrations', children=[
            ChildItem(model='demo.city'),
        ]),
        ParentItem('Users', children=[
            ChildItem(model='auth.user'),
            ChildItem('User groups', 'auth.group'),
        ], icon='fa fa-users'),
        ParentItem('Right Side Menu', children=[
            ChildItem('Password change', url='admin:password_change'),
            ChildItem('Open Google', url='http://google.com', target_blank=True),

        ], align_right=True, icon='fa fa-cog'),
    )
    '''

    '''
    menu = (
        ParentItem(app='questionnaire'),
        ParentItem('Пользователи', children=[
            ChildItem(model='main.CustomUser'),
            ChildItem(model='auth.Group'),
            ChildItem('Open Google', url='http://google.com', target_blank=True),
        ]),
    )
    '''

    def menu_handler(self, items, request, context):
        main_group = None
        user_group = None
        for item in items:
            if item.label == MainConfig.verbose_name:
                main_group = item
            elif item.label == 'Пользователи и группы':
                user_group = item
        child = main_group.children[0]
        child.parent_item = user_group
        user_group.children.append(child)
        items.remove(main_group)
        return items
