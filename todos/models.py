from django.db import models


# Create your models here.
class Todo(models.Model):
    parent_list = models.ForeignKey(
        to="lists.List", related_name="todos", on_delete=models.CASCADE
    )

    title = models.CharField(max_length=255)

    is_complete = models.BooleanField(default=False)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-create_date"]
        indexes = [models.Index(fields=["-create_date"])]
