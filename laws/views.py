from django.shortcuts import render, redirect
from .models import LawList, Lawyers, DetailLaw
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


#To display Laws
@login_required()
def lawlist(request):
    lawlist = LawList.objects.all()
    return render(request, 'lawlist.html', {'lawlist':lawlist})


#detail view of each law
@login_required()
def detailaw(request, pk):
    law = DetailLaw.objects.filter(category=pk)
    return render(request, 'lawdetail.html', {'law':law})


#List of Lawyers
@login_required()
def lawyers(request):
    lawyers = Lawyers.objects.all()
    return render(request, 'lawyers.html', {'lawyers':lawyers})
    
    
#search result of laws
def searchlaw(request):
   if request.method == "GET":
       query = request.GET.get('query')
       if query:
           law = DetailLaw.objects.filter(description__icontains=query)
           return render(request, 'searchlaw.html',{'law':law} )
       else:
           print("no info to show")
           return render(request, 'searchlaw.html', {'law':law})
     
     
#search result of Lawyers       
def searchlawyer(request):
   if request.method == "GET":
       query = request.GET.get('query')
       if query:
           lawyers = Lawyers.objects.filter(section__icontains=query)
           return render(request, 'searchlawyers.html',{'lawyers':lawyers} )
       else:
           print("no info to show")
           return render(request, 'searchlawyers.html', {'lawyers':lawyers})
 
       
#send appointment request to lawyers
@login_required
def sendrequest(request, id):
    if request.method == 'POST':
       title = "Your Request Has Delivered"
       email = request.POST['email']
       lawyer = Lawyers.objects.filter(id=id).first()
       lawyer_name = lawyer.name
       section = lawyer.section
       reciever = request.user.username
       message = f"Dear {reciever},\n\nThank you for your email. We are pleased to confirm that your appointment request with {lawyer_name}({section}yer) has been successfully delivered.\n\nYou will receive updates regarding your appointment soon. If you have any questions or need further assistance, feel free to reach out.\n\nBest regards,\nLawSystem\nContact Information : lawsystem2024@gmail.com\n"
       
       send_mail(
           title,#title
           message, #message
           'settings.EMAIL_HOST_USER', #sender if not available
           [email],
           fail_silently=False
       )
       return redirect('lawyers')
    return render(request, 'sendrequest.html')


def court_details(request):
    return render(request, "court_details.html")