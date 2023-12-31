from django import template

register = template.Library()

@register.filter(name='sort_by_likes')
def sort_by_likes(products):
    """
    Custom filter to sort products by likes count in descending order.
    """
    return sorted(products, key=lambda x: x.likes.count() if hasattr(x.likes, 'count') else 0, reverse=True)

@register.filter(name='sort_by_date')
def sort_by_date(products):
    """
    Custom filter to sort products by date in descending order.
    """
    return sorted(products, key=lambda x: x.date_field, reverse=True)