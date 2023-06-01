from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import CustomAccount, LogIn
from .serializers import CustomAccountSerializer, LogInSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class RegisterApi(APIView):

    @swagger_auto_schema(request_body=CustomAccountSerializer,
                         operation_summary="This endpoint allows to register an account",
                         operation_description="fields required are email, name and password. Raises an error if user is trying to create existing email")
    def post(self, request):
        serializer = CustomAccountSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LogInApi(APIView):
    @swagger_auto_schema(request_body=LogInSerializer,
                         operation_summary="This endpoint allows to generate TOKEN",
                         operation_description="This generates a TOKEN based on the given credentials, raises an error if credentials is invalid")
    def post(self, request):
            serializer = LogInSerializer(data=request.data)
            if serializer.is_valid():
                user = authenticate(email=serializer.data['email'], password=serializer.data['password'])
                print(user)
                if user is None:
                    return Response({'message': 'invalid email and password'}, status=status.HTTP_404_NOT_FOUND)
                token = Token.objects.get_or_create(user=user)
                return Response({'message': 'successfully logged in', 'token': user.auth_token.key},
                                status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

