from enum import Enum
from uuid import uuid4

from django.db import models
from django.db.models import *


class Author(models.Model):
    first_name = models.CharField(max_length=250, blank=False, null=False)
    last_name = models.CharField(max_length=250, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class LibraryUser(models.Model):
    # user_id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Language(Enum):
    NONE = '-choose-'
    ENGLISH = 'Eng'
    FRENCH = 'Frn'
    SPANISH = 'Spn'
    PORTUGUESE = 'Por'
    YORUBA = 'Yor'
    DUTCH = 'Dch'


class Genre(Enum):
    NONE = '-choose-'
    HORROR = 'Horror'
    SCIENCE_AND_FICTION = 'Sci-fi'
    ADVENTURE = 'Adventure'
    DOCUMENTARY = 'Documentary'
    ROMANCE = 'Romance'


class Book(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    author = models.ForeignKey(Author, on_delete=CASCADE, default=None, related_name='Author')
    summary = models.TextField(blank=False, null=False)
    ISBN = models.CharField(max_length=45, blank=False, null=False)
    genre = models.CharField(choices=[(genre.value, genre.name) for genre in Genre],
                             max_length=60, default=Genre.NONE.value)
    language = models.CharField(choices=[(language.value, language.name) for language in Language],
                                max_length=75, default=Language.NONE.value)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class LoanStatus(Enum):
    AVAILABLE = 'Available'
    REQUESTED = 'Requested'
    ISSUED = 'Issued'
    RETURNED = 'Returned'
    OVERDUE = 'Overdue'
    CANCELLED = 'Cancelled'


class BookInstance(models.Model):
    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    due_back = models.DateField()
    status = models.CharField(choices=[(status.name, status.value) for status in LoanStatus],
                              max_length=45, default='Available')
    book = models.ForeignKey(Book, on_delete=CASCADE, related_name='Book')
    imprint = models.CharField(max_length=350)
    borrower = models.ForeignKey(LibraryUser, on_delete=PROTECT)

    def __str__(self):
        return f'{self.imprint}, {self.book}'
