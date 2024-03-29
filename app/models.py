from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=40)
    age = models.IntegerField()
    contactno=models.BigIntegerField(unique=True,max_length=10)
    gender=models.CharField(max_length=20)
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)

    def __str__(self):
       return self.name


class Adminlogin(models.Model):
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)



# class ModelASerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ModelA
#         fields = '__all__'
#         depth = 1
