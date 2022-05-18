from pickle import FROZENSET
from django.shortcuts import render
from about.models import About
from contact.models import Contact
from projects.models import Projects, Category
# Create your views here.





def dashboard(request):
    about = About.objects.all().last()
    contact = Contact.objects.all().last()
    projects = Projects.objects.all()
    categories = Category.objects.all()
    context = {
        'about':about,
        'contact':contact,
        'projects':projects,
        'categories':categories
    }

    return render(request, 'users/dashboard.html', context)