from rest_framework import serializers
from .models import StudentDetails

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
       model=StudentDetails
       fields=['id','Name','Contact','Address']