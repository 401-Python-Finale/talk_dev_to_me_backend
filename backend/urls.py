from django.urls import path
from .views import UserList, UserDetail

urlpatterns = [
    path('', UserList.as_view(), name='User_list'),
    path('<int:pk>/', UserDetail.as_view(), name='User_detail'),
    
]