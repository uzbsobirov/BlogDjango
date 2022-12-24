from django.shortcuts import render, get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ToDo
from django.forms import model_to_dict
from .serializer import ToDoSerializer

@api_view(http_method_names=['GET', 'POST'])
def todo_list(request: Request):
    if request.method == 'GET':
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(instance=todos, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = ToDoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)



















# @api_view(http_method_names=['GET', 'POST'])
# def todo_list(request: Request):
#     if request.method == "POST":
#         title = request.data.get('title')
#         description = request.data.get('description')
#         todo = ToDo.objects.create(title=title, description=description)
#         return Response({"todo": model_to_dict(todo)})
#     todos = ToDo.objects.all().values()
#     return Response({"todos": list(todos)})
#
#
# @api_view(http_method_names=['GET', 'PUT', 'DELETE', 'PATCH'])
# def get_todo_detail(request: Request, todo_id: int):
#     todo = get_object_or_404(ToDo, pk=todo_id)
#     if request.method == 'GET':
#         return Response({"todo": model_to_dict(todo)})
#     elif request.method == 'PUT':
#         title = request.data.get('title')
#         description = request.data.get('description')
#         complited = request.data.get('complited')
#         todo.title = title
#         todo.description = description
#         todo.complited = complited
#         todo.save()
#         return Response({"updated": model_to_dict(todo)})
#     elif request.method == 'DELETE':
#         todo.delete()
#         return Response({"deleted": f"{todo_id} was successfully deleted"})
#     elif request.method == 'PATCH':
#         complited = request.data.get('complited')
#         todo.complited = complited
#         todo.save()
#         return Response({"updated": model_to_dict(todo)})
#
