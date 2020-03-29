from django.urls import path
from . import views

urlpatterns = [
    path('article/<int:id>/', views.article, name="article"),
    path('articles', views.articles, name="articles"),
    path('titles', views.titles, name="titles"),
    path('comments', views.comments, name="comments"),
    path('likes', views.likes, name="likes"),
    path('', views.home, name="home"),
]