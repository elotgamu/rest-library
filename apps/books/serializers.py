from rest_framework import serializers

from .models import Book, Author, Editorial, BooksEditorials


class EditorialListSerializer(serializers.ModelSerializer):
    """Serializer to get Editorial"""
    class Meta:
        model = Editorial
        fields = ('id', 'name',)


class BookEditorialSerializer(serializers.ModelSerializer):
    """ Serializer Class for the M2M model Books/Editorial """
    editorial = serializers.ReadOnlyField(source='editorial.id')
    editorial_name = serializers.ReadOnlyField(source='editorial.name')

    class Meta:
        model = BooksEditorials
        fields = ('editorial', 'editorial_name', 'quantity',)


class BookEditorialCreateSerializer(serializers.ModelSerializer):
    """ Serializer for Book Editorial M2M through model"""

    class Meta(object):
        model = BooksEditorials
        fields = ('editorial', 'quantity',)


class BookListSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for books list"""
    class Meta:
        model = Book
        fields = ('id', 'title', 'url')


class BasicAuthorSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for showing basic author data in books details"""
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'url')


class BookDetailSerializer(serializers.ModelSerializer):
    """Serializer class for book detail"""
    authors = BasicAuthorSerializer(many=True, read_only=True)
    editorials = BookEditorialSerializer(source='bookseditorials_set',
                                         many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'authors', 'editorials',)


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    """API serializer for Author model"""
    books = BookListSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('url', 'id', 'first_name', 'last_name', 'bio', 'books',)


class BookCreateSerializer(serializers.ModelSerializer):
    """API serializer for Book model instances"""
    registered_by = serializers.ReadOnlyField(source='registered_by.username',)
    authors = BasicAuthorSerializer(read_only=True, many=True)
    authors_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        write_only=True, many=True)

    editorials = BookEditorialCreateSerializer(many=True, write_only=True)
    editorials_list = BookEditorialSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'description',
                  'registered_by', 'authors', 'authors_id',
                  'editorials',
                  'editorials_list',
                  )

    def create(self, validated_data):
        """ Override the create method to write on m2m nested fields """
        editorials = validated_data.pop('editorials')
        authors = validated_data.pop('authors_id')
        book = Book.objects.create(**validated_data)

        for author in authors:
            book.authors.add(author)

        for editorial in editorials:
            print(editorial)
            data = dict(editorial)
            BooksEditorials.objects.create(book=book,
                                           editorial=data['editorial'],
                                           quantity=data['quantity']
                                           )

        return book

    def update(self, instance, validated_data):
        """
            Override the update method to write on nested m2m related fields
        """
        instance.title = validated_data.pop('title')
        instance.description = validated_data.pop('description')

        if validated_data['authors_id']:

            authors_received = validated_data.pop('authors_id')
            for author in authors_received:
                instance.authors.add(author)

            """
            If the author not in the request therefore remove it
            """
            for author in instance.authors.all():

                if author not in authors_received:
                    instance.authors.remove(author)

        instance.save()
        return instance
