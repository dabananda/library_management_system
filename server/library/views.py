from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from library.models import Author, Book, Member, BorrowRecord
from .serializers import AuthorSerializer, BookSerializer, MemberSerializer, BorrowRecordSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsLibrarian, IsMember


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsLibrarian()]
        return [IsAuthenticated()]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsLibrarian()]
        return [IsAuthenticated()]


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsLibrarian]


class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsLibrarian()]
        return [IsAuthenticated()]


@api_view(['POST'])
def borrow_book(request):
    try:
        book_id = request.data['book']
        member_id = request.data['member']
        book = Book.objects.get(id=book_id)

        if not request.user.groups.filter(name='Member').exists():
            return Response({'error': 'Only members can borrow books'}, status=status.HTTP_403_FORBIDDEN)

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

        if not request.user.groups.filter(name='Member').exists():
            return Response({'error': 'Only members can return books'}, status=status.HTTP_403_FORBIDDEN)

        if record.return_date:
            return Response({'error': 'Book already returned'}, status=status.HTTP_400_BAD_REQUEST)

        record.return_date = timezone.now().date()
        record.book.availability_status = True
        record.book.save()
        record.save()

        return Response({'message': 'Book returned successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
