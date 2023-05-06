from django.contrib import admin
from .models import StudentDetails

# Register your models here.
#admin.site.register(StudentDetails)
@admin.register(StudentDetails)
class StudentDetailsAdmin(admin.ModelAdmin):
    list_display=['id','Name','Contact','Address']


