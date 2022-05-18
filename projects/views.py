from django.shortcuts import get_object_or_404, render
from .models import Projects, Category

# Create your views here.



def projects(request):
    projects = Projects.objects.all()
    context = {'projects':projects}

    return render(request, 'projects/projects.html', context)



def project(request, p_id):
    project = get_object_or_404(Projects, pk=p_id)
    context = {'project':project}

    return render(request, 'projects/project.html', context)



def categories(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    

    return render(request, 'projects/categories.html', context=context)    


def category(request, c_id): 
    category = get_object_or_404(Category, pk=c_id)
    projects = Projects.objects.filter(category=category)
    context = {
        'category':category,
        'projects':projects
        }

    return render(request, 'projects/category.html', context=context)
