from rest_framework import  serializers
from rest_framework.renderers import JSONRenderer

# ToDo Model obyektlarni olish uchun
class ToDoModel:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

# ToDo Serializer
class ToDoSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    completed = serializers.BooleanField(default=False)

# encode func
def encode():
    model = ToDoModel(title="Kechqurun kitob o'qish", description="Har kuni kechqurun kitob o'qish")
    model_sr = ToDoSerializer(instance=model)
    print(model_sr.data, type(model_sr.data), sep="  va  ")
    json = JSONRenderer().render(model_sr.data)
    print(json)

