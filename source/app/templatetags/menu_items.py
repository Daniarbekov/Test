from django import template
from django.shortcuts import get_object_or_404
from app.models import MenuItems


register = template.Library()


@register.inclusion_tag('menu_temp.html', takes_context=True)
def draw_menu(context, name):
    menu = get_object_or_404(MenuItems, name=name)
    current_url = context['request'].path
    menu_context = {
        'menu_items': menu,
        'current_url': current_url
        }
    return menu_context
