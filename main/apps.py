from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class MainConfig(AppConfig):
    name = 'main'
    verbose_name = 'Основное'


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'

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
