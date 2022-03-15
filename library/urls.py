from django.urls import path

from library.views import BooksView, BookView

urlpatterns = [
    path('v1/library/books', BooksView.as_view()),
    path('v1/library/book/<pk>/', BookView.as_view()),
]
