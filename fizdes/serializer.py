import io
from rest_framework.parsers import JSONParser
from rest_framework import  serializers
from rest_framework.renderers import JSONRenderer
from .models import ToDo
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
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return ToDo.objects.create(**validated_data)

# encode func
def encode():
    model = ToDoModel(title="Kechqurun kitob o'qish", description="Har kuni kechqurun kitob o'qish")
    model_sr = ToDoSerializer(instance=model)
    json = JSONRenderer().render(model_sr.data)
    print(json)

def decode():
    stream = io.BytesIO(b'{"title":"Kechqurun kitob o\'qish","description":"Har kuni kechqurun kitob o\'qish","completed":false}')
    data = JSONParser().parse(stream)
    serializer = ToDoSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)