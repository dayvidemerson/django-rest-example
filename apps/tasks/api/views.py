from rest_framework import viewsets
from rest_framework import generics

from ..models import Task

from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    