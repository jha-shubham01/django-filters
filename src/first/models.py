from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32, null=False)

    def __str__(self) -> str:
        return self.name
    

class RandomList(models.Model):
    category = models.ForeignKey(Category, related_name="random_list", on_delete=models.CASCADE)
    name = models.CharField(max_length=32, null=False)
    description = models.TextField(null=True)


    def __str__(self) -> str:
        return self.name