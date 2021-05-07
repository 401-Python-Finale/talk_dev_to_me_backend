from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import User_ProfileSerializer 
from .models import User_Profile
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from backend.permissions import IsOwnerOrReadOnly

class UserList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,) 
    queryset = User_Profile.objects.all()
    serializer_class = User_ProfileSerializer

 
class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = User_Profile.objects.all()
    serializer_class = User_ProfileSerializer