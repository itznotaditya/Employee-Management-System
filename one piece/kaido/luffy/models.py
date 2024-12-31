from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    designation = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    image = models.ImageField(upload_to='employee_images/', blank=True, null=True)

    def __str__(self):
        return self.name

