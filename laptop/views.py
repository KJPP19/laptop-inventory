from django.shortcuts import render
from .models import UserInfo, Laptop, DamagedUnit
from .serializers import( UserInfoSerializer, LaptopSerializer, 
                         LaptopSummarySerializer, LaptopStatusSerializer,
                         LaptopCurrentUserSerializer, DamagedUnitSerializer,
                         LaptopDetailedViewSerializer)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter, SearchFilter
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import logging

logger = logging.getLogger(__name__)


class UserInfoList(ListAPIView):
    
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    pagination_class = PageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(operation_summary="This endpoint fetch the list of user's info ",
                         operation_description="Since this endpoint shows the data about the user, " 
                         "in order to access this endpoint, you must be the admin. "
                         "this endpoint contains user's name, email and phone number. " 
                         "These will be the current users of a certain laptop. Pagination is implemented here, 3 user's infor per page")
    def get(self, request, *args, **kwargs):
        logger.debug('fetching user info')
        return super().get(request, *args, **kwargs)


class UserInfoCreate(APIView):
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(request_body=UserInfoSerializer,
                         operation_summary="This endpoint allows to create new user info",
                         operation_description="Since this endpoint shows the data about the user," 
                         "in order to access this endpoint, you must be the admin."
                         "this endpoint expects value field user's name, email and phone number. Does not allow creation of existing user email and phone number, "
                         "assuming that only philippine number is used where it contains 11 digit number(09xxxxxxxxx), raise an error if the contact number has less than or greater than 11, "
                         "also raises an error when contact number contains non numeric values." 
                         "These will be the current users of a certain laptop")
    def post(self, request):
        logger.debug('creating new user info')
        serializer = UserInfoSerializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('user info created')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            logger.error(f'validation error: {e.detail}')
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception('error creating user info')
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserInfoDetailApi(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]
    @swagger_auto_schema(operation_summary="This endpoint allows to fetch single user's info based on the given ID",
                         operation_description="Since this endpoint shows the data about the user," 
                         "nn order to access this endpoint, you must be the admin.")
    def get(self, request, user_id):
        logger.debug('fetching single user info')
        userinfo_item = get_object_or_404(UserInfo, pk=user_id)
        serializer = UserInfoSerializer(userinfo_item)
        logger.info('successfully fetched')
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=UserInfoSerializer,
                         operation_summary="This endpoint allows to update user's info data",
                         operation_description="Since this endpoint shows the data about the user," 
                         "nn order to access this endpoint, you must be the admin.")
    def put(self, request, user_id):
        logger.debug('updating user info')
        userinfo_item = get_object_or_404(UserInfo, pk=user_id)
        serializer = UserInfoSerializer(userinfo_item, data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('user info updated')
            return Response(serializer.data, status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            logger.error(f'validation error: {e.detail}')
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @swagger_auto_schema(operation_summary="This endpoint allows to delete user's info data",
                         operation_description="Since this endpoint shows the data about the user," 
                         "nn order to access this endpoint, you must be the admin.")  
    def delete(self, request, user_id):
        userinfo_item = get_object_or_404(UserInfo, pk=user_id)
        try:
            userinfo_item.delete()
            logger.info('user info deleted')
            return Response({'message': 'user info has been deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LaptopApi(ListAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['brand', 'model', 'PO_number', 'serial_number']
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(operation_summary="This endpoint fetch the list of Laptops",
                         operation_description="User must be TOKEN authenticated, specific laptops info about the brand, "
                         "model, order number, serial number, status and current user ID. " 
                         "pagination and searchability('brand', 'model', 'PO_number', 'serial_number') is implemented")
    def get(self, request, *args, **kwargs):
        logger.debug('fetching laptop list')
        return super().get(request, *args, **kwargs)


class LaptopCreate(APIView):
    
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(request_body=LaptopSerializer,
                         operation_summary="This endpoint allows to create new Laptop ",
                         operation_description="User must be TOKEN authenticated, current_user can be leave as blank, where it will be stored "
                         "as NULL in the database. raises an error when user is trying to create an existing serial number and order number. "
                         "Assuming that serial number and order number can contain both numeric and non-numeric values." 
                         "Status is set to have a valid choice(available, assigned and decommissioned), raises an error if invalid.")
    def post(self, request):
        logger.debug('creating new laptop info')
        serializer = LaptopSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('new laptop created')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            logger.error(f'validation error: {e.detail}')
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LaptopDetailApi(APIView):
    """updates all fields of laptop including current user and laptop status"""
    
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    @swagger_auto_schema(operation_summary="This endpoint fetch a single Laptop based on the given ID",
                         operation_description="User must be TOKEN authenticated")
    def get(self, request, laptop_id):
        logger.debug('fetching single laptop info')
        laptop = get_object_or_404(Laptop, pk=laptop_id)
        logger.debug('retrieving laptop id')
        serializer = LaptopSerializer(laptop)
        logger.info('laptop fetched')
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=LaptopSerializer,
                         operation_summary="This endpoint allows to update existing Laptop ",
                         operation_description="User must be TOKEN authenticated, updates all fields of laptop including current user and laptop status")
    def put(self, request, laptop_id):
        logger.debug('updating single laptop')
        laptop = get_object_or_404(Laptop, pk=laptop_id)
        serializer = LaptopSerializer(laptop, data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('laptop updated')
            return Response(serializer.data, status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            logger.error(f'validation error: {e.detail}')
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @swagger_auto_schema(operation_summary="This endpoint delete a single Laptop",
                         operation_description="User must be TOKEN authenticated")
    def delete(self, request, laptop_id):
        logger.debug('fetching single laptop')
        laptop = get_object_or_404(UserInfo, pk=laptop_id)
        try:
            laptop.delete()
            logger.info('laptop deleted')
            return Response({'message': 'laptop info has been deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LaptopSummaryApi(ListAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSummarySerializer
    pagination_class = PageNumberPagination
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    @swagger_auto_schema(operation_summary="This endpoint fetch the list of laptops limited data fields",
                         operation_description="User must be TOKEN authenticated, this shows the laptop model, status and the current user name")
    def get(self, request, *args, **kwargs):
        logger.debug('fetching laptop list gaving limited data fields')
        return super().get(request, *args, **kwargs)


class LaptopDetailedView(ListAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopDetailedViewSerializer
    pagination_class = PageNumberPagination
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(operation_summary="This endpoint fetch the list of laptops where current user is nested",
                         operation_description="User must be ADMIN since the response will be the laptop and the current user info,")
    def get(self, request, *args, **kwargs):
        logger.debug('fetching laptop detailed info')
        return super().get(request, *args, **kwargs)

class LaptopAvailableStatus(ListAPIView):
    """LaptopSummarySerializer can be used to show limited data fields"""
    queryset = Laptop.objects.filter(status='available')
    serializer_class = LaptopSerializer
    pagination_class = PageNumberPagination
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    @swagger_auto_schema(operation_summary="This endpoint fetch the list of laptops where status is available",
                         operation_description="this endpoint is filtered out where it only shows laptop where its status is available")
    def get(self, request, *args, **kwargs):
        logger.debug('fetching available laptops')
        return super().get(request, *args, **kwargs)

class LaptopAssignedStatus(ListAPIView):
    """LaptopSummarySerializer can be used to show limited data fields"""
    queryset = Laptop.objects.filter(status='assigned')
    serializer_class = LaptopSerializer
    pagination_class = PageNumberPagination
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    @swagger_auto_schema(operation_summary="This endpoint fetch the list of laptops where status is assigned",
                         operation_description="this endpoint is filtered out where it only shows laptop where its status is assigned")
    def get(self, request, *args, **kwargs):
        logger.debug('fetching assigned laptops')
        return super().get(request, *args, **kwargs)

class LaptopDecommissionedStatus(ListAPIView):
    """LaptopSummarySerializer can be used to show limited data fields"""
    queryset = Laptop.objects.filter(status='decommisioned')
    serializer_class = LaptopSerializer
    pagination_class = PageNumberPagination
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(operation_summary="This endpoint fetch the list of laptops where status is decommissioned",
                         operation_description="this endpoint is filtered out where it only shows laptop where its status is decommissioned")
    def get(self, request, *args, **kwargs):
        logger.debug('fetching decommissioned laptops')
        return super().get(request, *args, **kwargs)

class UpdateLaptopStatusApi(APIView):
    """assummed that status is updated frequently"""
   
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
   
    @swagger_auto_schema(request_body=LaptopStatusSerializer,
                         operation_summary="This endpoint allows to update only the specific laptop status",
                         operation_description="User must be TOKEN authenticated, updates only the specific laptop status")
    def patch(self, request, laptop_id):
        logger.debug('updating laptop status')
        laptop = get_object_or_404(Laptop, pk=laptop_id)
        serializer = LaptopStatusSerializer(laptop, data=request.data, partial=True)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('laptop status updated')
            return Response(serializer.data, status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            logger.error(f'validation error: {e.detail}')
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class UpdateLaptopCurrentUser(APIView):
    
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    @swagger_auto_schema(request_body=LaptopCurrentUserSerializer,
                         operation_summary="This endpoint allows to update only the specific laptop current user",
                         operation_description="User must be TOKEN authenticated, updates only the specific laptop current user")
    def patch(self, request, laptop_id):
        logger.debug('updating laptop current user')
        laptop = get_object_or_404(Laptop, pk=laptop_id)
        serializer = LaptopCurrentUserSerializer(laptop, data=request.data, partial=True)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('updated current user')
            return Response(serializer.data, status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            logger.error(f'validation error: {e.detail}')
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DamagedUnitApi(APIView):
    
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(operation_summary="This endpoint allows to fetch list of damages made by a specific user",
                         operation_description="User must be TOKEN authenticated, this shows the specific user, the laptop that was damaged, "
                         "damage type and a description")
    def get(self, request):
        logger.debug('fetching damaged laptops')
        damages = DamagedUnit.objects.all()
        serializer = DamagedUnitSerializer(damages, many=True)
        logger.info('fetched')
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=DamagedUnitSerializer,
                        operation_summary="This endpoint creates a new damaged laptop",
                        operation_description="User must be TOKEN authenticated, "
                        "damage type is set to have a valid choice(minor, major, severe) raises error when damage type is invalid")
    def post(self, request):
        serializer = DamagedUnitSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('damage report created')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            logger.error(f'validation error: {e.detail}')
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class DamagedUnitDetail(APIView):
    
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    @swagger_auto_schema(operation_summary="This endpoint allows to fetch a single damage made by a specific user",
                         operation_description="User must be TOKEN authenticated, this shows the specific user, the laptop that was damaged, "
                         "damage type and a description")
    def get(self, request, damage_id):
        damage = get_object_or_404(DamagedUnit, pk=damage_id)
        serializer = DamagedUnitSerializer(damage)
        logger.info('fetched single damage report')
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=DamagedUnitSerializer,
                        operation_summary="This endpoint updates existing damaged laptop",
                        operation_description="User must be TOKEN authenticated, "
                        "damage type is set to have a valid choice(minor, major, severe) raises error when damage type is invalid")
    def put(self, request, damage_id):
        damage = get_object_or_404(damage_id, pk=damage_id)
        serializer = DamagedUnitSerializer(damage, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('damage report updated')
            return Response(serializer.data, status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            logger.error(f'validation error: {e.detail}')
            return Response({'error': e.detail }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(request_body=DamagedUnitSerializer,
                        operation_summary="This endpoint deletes existing damaged laptop",
                        operation_description="User must be TOKEN authenticated")
    def delete(self, request, damage_id):
        damage = get_object_or_404(damage_id, pk=damage_id)
        try:
            damage.delete()
            return Response({'message': 'damage detail has been deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)