
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    
   path('', views.lawlist, name='lawlist'),
   path('detailaw/<str:pk>/', views.detailaw, name='detailaw'),
   path('lawyers/', views.lawyers, name='lawyers'),
   path('searchlaw/', views.searchlaw, name='searchlaw'),
   path('searchlawyer/', views.searchlawyer, name='searchlawyer'),
   path('sendrequest<int:id>/', views.sendrequest, name='sendrequest'),
   path('court/', views.court_details, name='court_details'),
   path('case/', views.case, name='case'),
   path('filecase/', views.file_case, name='filecase'),
   path('delete/<str:id>/', views.delete_case, name='delete_case'),
   path('edit/<str:case_id>/', views.edit_case, name='edit_case'),
   path('casedeclaration/<str:id>/', views.case_declaration, name='casedeclaration'),
   
    
]
