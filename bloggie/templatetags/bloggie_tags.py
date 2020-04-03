from django import template

register = template.Library()

from ..models import Post

@register.simple_tag(name='total_posts') #Dzięki 'name', możliwa dowolna nazwa znacznika
def total_posts():
    return Post.published.count()

@register.inclusion_tag('bloggie/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}
