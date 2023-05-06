from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import StudentDetails
from .serializers import StudentSerializers
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def Home(request):
    #return HttpResponse("Hi! Welcome to the innovation with python training.")
    return render(request,'FIRSTAPPLICATION/Home.html')

def getDetails(request):
    try:
        all_students=StudentDetails.objects.all()
    except:
        return HttpResponse("records not found", status= 404)
    
    if request.method=='GET':
        studentList=StudentSerializers(all_students,many=True)
        return JsonResponse(studentList.data,safe=False)
    
@csrf_exempt     
def addDetails(request):
    # try:
    #     all_students=StudentDetails.objects.all()
    # except:
    #     return HttpResponse("Records are not found",status=404)
    
    if request.method=='POST':
        body=JSONParser().parse(request)
        studentList=StudentSerializers(data=body)
        
        if studentList.is_valid():
            studentList.save()
            return JsonResponse(studentList.data,status=201)
        else:
            return HttpResponse("Record is not added", status=400)

def getDetailsbyId(request,id):
    try:
        student=StudentDetails.objects.get(id=id)
    except:
        return HttpResponse("Record not found",status=404)
    
    if request.method=='GET':
        studentById=StudentSerializers(student)
        return JsonResponse(studentById.data,status=200)

@csrf_exempt
def updatedetails(request,id):
    try:
        student=StudentDetails.objects.get(id=id)
    except:
        return HttpResponse("Records not found",status=400)
    
    if request.method=='PUT':
        body=JSONParser().parse(request)
        studentList=StudentSerializers(student,data=body)
        
        if studentList.is_valid():
            studentList.save()
            return JsonResponse(studentList.data,status=200)
        else:
            return HttpResponse("Not Updated",status=404)
        
@csrf_exempt
def deleteDetails(request,id):
    try:
        student=StudentDetails.objects.get(id=id)
    except:
        return HttpResponse("Record not Found", status=404)
    
    if request.method=='DELETE':
        student.delete()
        return HttpResponse("Record deleted",status=204)


