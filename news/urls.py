from django.urls import path
from .views import (
                     PostList, NewsList,
                     PostDetail, NewsDetail,
                     PostCreate, NewsCreate,
                     PostEdit, NewsEdit,
                     PostDelete, NewsDelete,
                     NewsSearch, subscriptions
)


urlpatterns = [

    # path('', PostList.as_view(), name='post_list'),
    path('news/', NewsList.as_view(), name='news_list'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('news/search/', NewsSearch.as_view(), name='news_search'),
    path('post/', PostList.as_view(), name='post_list'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
]