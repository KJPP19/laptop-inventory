from django.urls import path
from .views import (UserInfoList, UserInfoCreate, UserInfoDetailApi, 
                    LaptopApi, LaptopCreate, LaptopDetailApi, 
                    LaptopSummaryApi, UpdateLaptopStatusApi, 
                    LaptopAvailableStatus, LaptopDecommissionedStatus,
                    LaptopAssignedStatus, UpdateLaptopCurrentUser, 
                    DamagedUnitApi, DamagedUnitDetail, LaptopDetailedView)


urlpatterns = [
    path('users/', UserInfoList.as_view()),
    path('users/add/', UserInfoCreate.as_view()),
    path('users/<int:user_id>/', UserInfoDetailApi.as_view()),
    path('laptops/', LaptopApi.as_view()),
    path('laptops/add/', LaptopCreate.as_view()),
    path('laptops/<int:laptop_id>/', LaptopDetailApi.as_view()),
    path('laptops/<int:laptop_id>/status/', UpdateLaptopStatusApi.as_view()),
    path('laptops/<int:laptop_id>/current-user/', UpdateLaptopCurrentUser.as_view()),
    path('laptops/status/assigned/', LaptopAssignedStatus.as_view()),
    path('laptops/status/available/', LaptopAvailableStatus.as_view()),
    path('laptops/status/decommissioned/', LaptopDecommissionedStatus.as_view()),
    path('damages/', DamagedUnitApi.as_view()),
    path('damages/<int:damage_id>/', DamagedUnitDetail.as_view()),
    path('summary/', LaptopSummaryApi.as_view()),
    path('laptops-detail/', LaptopDetailedView.as_view())
]
