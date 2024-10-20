from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# Create a new task and list all tasks
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Retrieve, update, or delete a specific task
class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
