from rest_framework import serializers
from .models import Author, Book
from datetime import date
# Bookserializer facilitates Book Model instances to be rendered in JSON format
# All fields are serialized and deserialized. 
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    #Validate publication_year
    def validate_publication_year(self, value):
        if value > date.today():
            return serializers.ValidationError('Publication year should not be in future.')
        return value

#AuthorSerializer converts Author Model instances to JSON format for easy rendering in API
#AuthorSerializer nests BookSerializer to serialize related books dynamically.
class AuthorSerializer(serializers.ModelSerializer):
    #Nested Book serializer to serialize related books dynamically
    books = serializers.SerializerMethodField(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']