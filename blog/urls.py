from django.urls import path,include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='blog_list'),
    path('<int:pk>',views.detail, name='detail')
]
