from rest_framework import serializers
from .models import Book
from drf_queryfields import QueryFieldsMixin


class BookSerializer(QueryFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'