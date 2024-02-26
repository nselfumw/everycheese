from django.urls import path 

from . import views

app_name = "books"
urlpatterns = [
    path(
        route='',
        view=views.BookListView.as_view(),
        name='list'
    ),
    path(
        route='authors/',
        view=views.AuthorListView.as_view(),
        name='author-list'
    ),
    path(
        route='<slug:slug>/', 
        view=views.BookDetailView.as_view(), 
        name='detail'
    ),
    path(
        route='authors/<slug:slug>/',
        view=views.AuthorDetailView.as_view(),
        name='author-detail'
    ),
]
