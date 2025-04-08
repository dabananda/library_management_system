from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books')
    ISBN = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=100)
    availability_status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    membership_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.member.name} borrowed {self.book.title}"


# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     username = models.CharField(
#         max_length=150, unique=False, blank=True, null=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email
