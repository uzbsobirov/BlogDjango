from django.urls import path
from .views import todo_list#, get_todo_detail


urlpatterns = [
    path('', todo_list, name="todo_list"),
    # path('<int:todo_id>/', get_todo_detail, name="get_todo_detail")
]

