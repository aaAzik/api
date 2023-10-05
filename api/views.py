from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.settings import *
from app.models import *
from .permissions import *
from .serializers import *

@api_view(['GET', 'POST'])
@permission_classes([UserPermission])
def user(request):
    if request.method == "GET":
        user = User.objects.all()
        serializer = UserSerializers(user, many=True, context = {'request': request})
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = HTTP_201_CREATED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
@permission_classes([UserDetailPermissions])
def user_detail(request, pk):
    user = User.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = UserSerializers(user)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = UserSerializers(user,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([TaskPermissions])
def task(request):
    if request.method == "GET":
        task = Task.objects.all()
        serializer = TaskSerializers(task, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = HTTP_201_CREATED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
@permission_classes([TaskDetailPermissions])
def task_detail(request, pk):
    task = Task.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = TaskSerializers(task)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = TaskSerializers(Task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([ProjectPermissions])
def project(request):
    if request.method == "GET":
        project = Project.objects.all()
        serializer = ProjectSerializers(project, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProjectSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = HTTP_201_CREATED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
@permission_classes([ProjectDetailPermissions])
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = ProjectSerializers(project)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = ProjectSerializers(project,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=HTTP_204_NO_CONTENT)



