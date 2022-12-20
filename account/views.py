from django.shortcuts import render
<<<<<<< HEAD

from django.shortcuts import render
=======
>>>>>>> 5ed3f1f13b5b8b3da94e0f9ee288d91f2c2c97fc
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .serializers import RegisterUserSerializer


class RegisterUserView(APIView):
    @swagger_auto_schema(request_body=RegisterUserSerializer())
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Вы успешно зарегистрировались", status=201)
<<<<<<< HEAD
=======

>>>>>>> 5ed3f1f13b5b8b3da94e0f9ee288d91f2c2c97fc
