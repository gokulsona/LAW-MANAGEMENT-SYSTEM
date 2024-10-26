from django.shortcuts import render
from laws.models import LawList
# Create your views here.

#index function. Home Page
def index(request):
    lawlist = LawList.objects.all()
    return render(request, 'index.html', {'lawlist':lawlist})


def about(request):
    return render(request, 'about.html')


def family_law(request):
    pass

