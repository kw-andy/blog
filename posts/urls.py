from django.urls import path
from .views import (BlogHome,
                    BlogPostCreate,
                    BlogPostEdit,
                    BlogPostDetail,
                    BlogPostDelete)

app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('create-article', BlogPostCreate.as_view(), name="create"),
    path('edit-article/<str:slug>', BlogPostEdit.as_view(), name="edit"),
    path('delete-article/<str:slug>', BlogPostDelete.as_view(), name="delete"),
    path('<str:slug>', BlogPostDetail.as_view(), name="detail"),
]