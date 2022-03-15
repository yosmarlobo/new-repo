from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from library.models import Book, Author
from library.serializers import BookSerializers, CreateBookSerializer, UpdateBookSerializer


class BooksView(APIView):

    # Listar todos los elementos
    def get(self, request):
        books = Book.objects.filter(is_active=True)
        serializers = BookSerializers(books, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    # Crear un elemento
    def post(self, request):
        # djando solo
        # name = request.data.get('name')

        # DRF => BODY -> parsear -> SERIALIZADORES => BookSerializers
        # print('REQUEST_DATA', request.data)

        serializer = CreateBookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # print('SERIALIZER_DATA', serializer.data)
            # YA TENEMOS EL BODY CONVERTIDO EN UN OBJETO
            book = serializer.save()  # SAVE
            data = BookSerializers(book).data
            return Response(data, status=status.HTTP_201_CREATED)


class BookView(APIView):

    # Detalle de un elemnto
    def get(self, request, pk):
        # try:
        #     book = Book.objects.filter(pk=pk, is_active=True).first() # id error => exeption
        # except:
        #     raise Http404()

        book = get_object_or_404(Book, pk=pk, is_active=True)
        serializers = BookSerializers(book)
        return Response(serializers.data, status=status.HTTP_200_OK)

    # Actualizar un elemento
    def put(self, request, pk):
        # only django
        # name = request.data.get('name')
        # print(name)
        # if name is None:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
        #
        # # Validar que exista el ID
        # book = Book.objects.filter(pk=pk).first()
        # book.name = name
        # book.save()

        book = Book.objects.filter(pk=pk).first()
        serializer = UpdateBookSerializer(book, data=request.data)

        serializer.is_valid(raise_exception=True)
        book = serializer.save()  # actualizer

        data = BookSerializers(book).data
        return Response(data, status=status.HTTP_200_OK)
        # serializer = UpdateBookSerializer(data=request.data)

    # Eliminar un elemento
    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk, is_active=True)
        book.is_active = False
        book.save()
        return Response(status=status.HTTP_202_ACCEPTED)
