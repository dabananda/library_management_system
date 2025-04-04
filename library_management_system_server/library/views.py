from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from library.models import Author, Book, Member, BorrowRecord
from .serializers import AuthorSerializer, BookSerializer, MemberSerializer, BorrowRecordSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer


@api_view(['POST'])
def borrow_book(request):
    try:
        book_id = request.data['book']
        member_id = request.data['member']
        book = Book.objects.get(id=book_id)

        if not book.availability_status:
            return Response({'error': 'Book not available'}, status=status.HTTP_400_BAD_REQUEST)

        BorrowRecord.objects.create(book=book, member_id=member_id)
        book.availability_status = False
        book.save()

        return Response({'message': 'Book borrowed successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def return_book(request):
    try:
        record_id = request.data['record_id']
        record = BorrowRecord.objects.get(id=record_id)

        if record.return_date:
            return Response({'error': 'Book already returned'}, status=status.HTTP_400_BAD_REQUEST)

        record.return_date = timezone.now().date()
        record.book.availability_status = True
        record.book.save()
        record.save()

        return Response({'message': 'Book returned successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
