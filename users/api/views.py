from rest_framework.decorators import permission_classes
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

from users.models import User
from users.api.serializers import UserSerializer

# endpoints Administrador


class UserApiViewSet(ModelViewSet):
    permission_clases = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()

# encriptar password users
    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)
# encriptar pasword para actualizar en patch y put

    def partial_update(self, request, *args, **kwargs):
        password = request.data['password']
        if password:
            request.data['password'] = make_password(password)
        else:
            request.data['password'] = request.user.password
        return super().update(request, *args, **kwargs)

# endpoints usuarios autenticados


class UserView(APIView):
    permissions_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
