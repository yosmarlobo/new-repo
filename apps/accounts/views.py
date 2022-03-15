from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import User


######################################################
## Listar el Perfil de un usuario mediante su PK
## usando django rest framework
######################################################
from apps.accounts.serializer import UserCustomSerializer


class UserView(APIView):

    def get(self, request, pk):
        user = User.objects.filter(pk=pk, is_active=True).first()
        serializer = UserCustomSerializer(user)
        return Response(serializer.data)
