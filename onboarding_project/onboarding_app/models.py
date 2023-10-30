from django.db import models

# Create your models here.
class Employee(models.Model):
    id= models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=False)
    department = models.CharField(max_length=100)
    start_date = models.DateField()
    in_onboarded = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


