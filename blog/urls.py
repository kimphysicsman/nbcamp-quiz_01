from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new_article, name='new_article'),
    path('category/', views.categorys, name='categorys'),
    path('article/', views.articles, name='articles'),
]