from django.db.models import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

'''
class TodoList(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
'''

# GET, POST


class TodoListCreateView(APIView):
    def get(self, request):
        queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET, PUT, PATCH, DETELE


class TodoDetailView(APIView):
    def get(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
