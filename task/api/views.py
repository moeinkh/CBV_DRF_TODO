from rest_framework import generics
from .serializers import TaskSerializer
from rest_framework import permissions
from task.models import Task
from rest_framework.response import Response

class TodoListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = TaskSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def get_queryset(self, *args, **kwargs):
    #     return super().get_queryset(*args, **kwargs).filter(user=self.request.user)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)    

class TodoDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
