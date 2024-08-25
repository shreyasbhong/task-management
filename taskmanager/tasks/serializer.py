from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class userRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password']

    def create(self,validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title','description','status','priority','due_date','created_at','updated_at','user']

