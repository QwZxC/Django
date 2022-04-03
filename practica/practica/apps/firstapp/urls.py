from django.urls import path
from . import views

appname = 'firstapp'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/comment', views.comment, name='comment'),
]