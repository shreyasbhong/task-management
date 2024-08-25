
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSets


router = DefaultRouter()
router.register(r'tasks', TaskViewSets, basename='tasks')

urlpatterns = [     
    path('', include(router.urls))                                                                                  ,
]