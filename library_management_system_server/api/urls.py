from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.views import (
    AuthorViewSet, BookViewSet, MemberViewSet, BorrowRecordViewSet,
    borrow_book, return_book
)

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
router.register('members', MemberViewSet)
router.register('borrow-records', BorrowRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('borrow/', borrow_book),
    path('return/', return_book),
]
