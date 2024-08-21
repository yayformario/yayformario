import pathlib
from django.shortcuts import render
from django.http import HttpResponse

#importing PageVisit model
from visits.models import PageVisit

#absolute path to the directory where the current script is located
this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *args, **kwargs):

    #Using a queryset to view page visits; stores everything
    #'qs' is common industry usage for query set
    qs = PageVisit.objects.all()

    #Page visit; counted filtered by anything using the current path
    page_qs = PageVisit.objects.filter(path=request.path)

    my_title = 'The home title from \'views.py\''
    my_context = {
        'page_title' : my_title,

        #Initialize query set
        "page_visit_count" : page_qs.count(),
        "total_visit_count" : qs.count(),

        #Can do math
        "percent": (page_qs.count()  / qs.count()) * 100.0
    }

    path = request.path
    print("path", path)

    #returning: render(request, templateName, contextName)
    html_template = "home.html"

    #Creating database from PageVisit
    PageVisit.objects.create(path = request.path)


    return render(request, html_template, my_context)

