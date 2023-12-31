from django import template

register = template.Library()

@register.filter(name='sort_by_likes')
def sort_by_likes(products):
    return sorted(products, key=lambda x: x.likes.count() if hasattr(x.likes, 'count') else 0, reverse=True)

@register.filter(name='sort_by_date')
def sort_by_date(products):
    return sorted(products, key=lambda x: x.updated_at if hasattr(x, 'updated_at') and x.updated_at else x.created_at, reverse=True)