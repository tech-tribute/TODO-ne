from django.db import models


# Create your models here.
class List(models.Model):
    name = models.CharField(
        max_length=255,
    )
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
