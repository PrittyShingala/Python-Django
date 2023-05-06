from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    Name=models.CharField(max_length=50)
    Contact=models.CharField(max_length=50)
    Address=models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.Name} {self.Contact} {self.Address}'
