from django.contrib import admin
from . import views
from django.urls import path, include
from .views import HomeView, ArticleDetailView, AddpostView, UpdatePostView, DeletePostView,LikeView

urlpatterns = [
    # path('',views.home,name='home'),
    path('', HomeView.as_view(), name='home'),
    path('details/<int:pk>', ArticleDetailView.as_view(), name='article_details'),
    path('add_post/', AddpostView.as_view(), name='add_post'),
    path('update/<int:pk>', UpdatePostView.as_view(), name='update_details'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('like/<int:pk>', LikeView, name="like_post"),
]
