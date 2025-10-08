from django.shortcuts import render
from django_redis import get_redis_connection
from django.core.cache import cache

# Create your views here.

def myview(request):
    # using django_redis and not internal django caching system
    # its a better way for large scale project to use redis 
    # but also you can use both django cache system and django-redis in single project
    r = get_redis_connection('default')

    r.set('name', 'nima_test_redis_in_django')

