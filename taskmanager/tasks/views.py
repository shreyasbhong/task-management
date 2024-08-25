import django_filters
from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .filters import TaskFilter
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import TaskSerializers, userRegistrationSerializer

# Create your views here.
class RegisterView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = userRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User Created Successfully"},status=status.HTTP_201_CREATED)
        return Response({"message":"Incorrect Credintials"},status=status.HTTP_400_BAD_REQUEST)
    
class TaskViewSets(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = TaskFilter
    search_fields = ['title', 'description']

class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {"message": "Hello, World!"}
        return Response(content)

