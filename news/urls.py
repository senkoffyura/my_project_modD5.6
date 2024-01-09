from django.urls import path
from django.views.decorators.cache import cache_page

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
    path('news/', cache_page(60*1)(NewsList.as_view()), name='news_list'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/', cache_page(60*5)(NewsDetail.as_view()), name='news_detail'),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('news/search/', NewsSearch.as_view(), name='news_search'),
    path('post/', cache_page(60*1)(PostList.as_view()), name='post_list'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>', cache_page(60*5)(PostDetail.as_view()), name='post_detail'),
    path('post/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
]