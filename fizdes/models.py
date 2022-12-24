from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    complited = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.title