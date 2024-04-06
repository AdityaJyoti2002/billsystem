from django.db import models

# Create your models here.
class GeneratePdf(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    field3 = models.CharField(max_length=100)
    field4 = models.CharField(max_length=100)
    field5 = models.CharField(max_length=100)
    field6 = models.CharField(max_length=100)
    field7 = models.CharField(max_length=100)
    
# class signups(models.Model):
#     email = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     cfm = models.CharField(max_length=100)
