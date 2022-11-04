from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
from .models import Book


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_queryset(self):
        fields : str = self.request.query_params.get('fields')
        fields_list = fields.split(',')
        if not fields:
            return super().get_queryset()
        return Book.objects.only('id')
        
        