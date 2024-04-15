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

class EmployeeCarDetails(models.Model):
    car_id = models.BigAutoField(primary_key=True)
    car_mode = models.CharField(max_length=50)

    def __str__(self):
        return self.car_mode

class Employee(models.Model):
    emp_id = models.BigAutoField(primary_key=True)
    emp_name = models.CharField(max_length=50)
    car = models.ManyToManyField(EmployeeCarDetails, blank=True)


    def save(self):
        super(Employee, self).save()
        val = EmployeeCarDetails.objects.get(car_id=1)
        self.car.add(val)

    def __str__(self):
        return str(self.emp_id)


# class User(AbstractUser):
# 
