from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.Home),
    path("getDetails/",views.getDetails),
    path("getDetailsbyId/<int:id>/",views.getDetailsbyId),
    path("addDetails/",views.addDetails),
    path("updatedetails/<int:id>/",views.updatedetails),
    path("deleteDetails/<int:id>/",views.deleteDetails),
]
