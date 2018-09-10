from django.db import models

from django.conf import settings

# Create your models here.


class Author(models.Model):
    # TODO: Define fields here
    first_name = models.CharField("author's first name", max_length=255)
    last_name = models.CharField("author's last name", max_length=255)
    bio = models.TextField("author small biography", blank=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    # TODO: Define custom methods here


class Editorial(models.Model):
    # TODO: Define fields here
    name = models.CharField("editorial's name", max_length=255)

    class Meta:
        verbose_name = "Editorial"
        verbose_name_plural = "Editorials"

    def __str__(self):
        return self.name

    # TODO: Define custom methods here


class Book(models.Model):
    # The book instances
    title = models.CharField("book title", max_length=255)
    description = models.TextField("book short description", blank=True)
    registered_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      related_name="books",
                                      on_delete=models.CASCADE)

    authors = models.ManyToManyField(Author, related_name="books")

    editorials = models.ManyToManyField(Editorial,
                                        through='BooksEditorials',
                                        through_fields=('book', 'editorial'))

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return "%s" % (self.title)

    # TODO: Define custom methods here


class BooksEditorials(models.Model):
    # Books and its publishings
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, blank=True, null=True)
