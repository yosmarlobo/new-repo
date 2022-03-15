from rest_framework import serializers

from library.models import Author, Book


class AuthorSerializers(serializers.ModelSerializer):
    # id en read_only por que es un dato que se genera en la BD
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = Author
        fields = ('id', 'name')


"""
    This serializer is using only for list o detail book
"""


class BookSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, )
    author = AuthorSerializers()
    name = serializers.CharField()
    publication_date = serializers.DateField()

    # def save(self, **kwargs):

    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'publication_date')


"""
    This serializer is using only for crete book 
"""


class CreateBookSerializer(serializers.ModelSerializer):
    author = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True, )
    publication_date = serializers.DateField(required=True)

    def validate_author(self, value):
        # 2 QUERYS A LA BD
        author = Author.objects.filter(pk=value)
        # query
        # LIST => len()
        # OBJECTO => None
        if len(author) == 0:
            raise serializers.ValidationError("Author doens't exist!")
        else:
            if author.first().is_active == False:
                raise serializers.ValidationError("deactivate")

        return value

    def save(self, **kwargs):
        book_data = self.validated_data
        author = book_data.pop('author', None)
        # author = Author.objects.first(pk=author_id) # Query al BD para obtener la instancia!
        book = Book.objects.create(author_id=author, **book_data)
        return book

    class Meta:
        model = Book
        fields = ('name', 'author', 'publication_date')


class UpdateBookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    def validate_name(self, value):
        if value is None:
            raise serializers.ValidationError({'Empty'})

        return value

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.email)
        instance.save()
        return instance

    class Meta:
        model = Book
        fields = ('name',)
