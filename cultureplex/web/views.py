from django.core.paginator import Paginator, InvalidPage, EmptyPage

from django.template import Context, loader
from web.models import Project
from web.models import Publication
from web.models import Person
from django.http import HttpResponse
from django.template import RequestContext


def projects(request):
    try:
        order = str(request.GET.get('orderby', '1'))
    except ValueError:
        page = 1
    projects_list = Project.objects.all().order_by('-active', 'name', 'contact')
    if order == 'contact':
        projects_list = Project.objects.all().order_by('contact', '-active', 'name')
    if order == 'name':
        projects_list = Project.objects.all().order_by('name', '-active', 'contact')
    paginator = Paginator(projects_list, 4) 
    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        projects = paginator.page(page)
    except (EmptyPage, InvalidPage):
        projects = paginator.page(paginator.num_pages)
    t = loader.get_template('Mprojects.html')
    c = RequestContext(request,{
        'projects': projects,
        'current_page': 'projects',
        'sort_criteria': request.GET.get('orderby')
    })
    return HttpResponse(t.render(c))

def project(request, project_id):
    project = Project.objects.get(pk=project_id)
    t = loader.get_template('Mproject.html')
    c = RequestContext(request,{
        'project': project,
        'current_page': 'projects'
    })
    return HttpResponse(t.render(c))

def publications(request):
    try:
        order = str(request.GET.get('orderby', '1'))
    except ValueError:
        page = 1
    publications_list = Publication.objects.all().order_by('title','publication_type','-publication_date','-aceptation_date')
    if order == 'publication_type':
        publications_list = Publication.objects.all().order_by('publication_type','title','-publication_date','-aceptation_date')
    if order == 'publication_date':
        publications_list = Publication.objects.all().order_by('-publication_date','title','publication_type','-aceptation_date')
    if order == 'acceptance_date':
        publications_list = Publication.objects.all().order_by('-aceptation_date','title','publication_type','-publication_date')
    paginator = Paginator(publications_list, 4) 
    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        publications = paginator.page(page)
    except (EmptyPage, InvalidPage):
        publications = paginator.page(paginator.num_pages)

    t = loader.get_template('Mpublications.html')
    c = RequestContext(request,{
        'publications': publications,
        'current_page': 'publications',
        'sort_criteria': request.GET.get('orderby')
    })
    return HttpResponse(t.render(c))

def publication(request, publication_id):
    publication = Publication.objects.get(pk=publication_id)
    t = loader.get_template('Mpublication.html')
    c = RequestContext(request,{
        'publication': publication,
        'current_page': 'publications'
    })
    return HttpResponse(t.render(c))

def persons(request):
    try:
        order = str(request.GET.get('orderby', '1'))
    except ValueError:
        page = 1
    persons_list = Person.objects.all().order_by('-active', 'name', 'position')
    if order == 'position':
        persons_list = Person.objects.all().order_by('position', '-active', 'name')
    if order == 'name':
        persons_list = Person.objects.all().order_by('name', '-active', 'position')
    paginator = Paginator(persons_list, 4) 
    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        persons = paginator.page(page)
    except (EmptyPage, InvalidPage):
        persons = paginator.page(paginator.num_pages)
    t = loader.get_template('Mpersons.html')
    c = RequestContext(request,{
        'persons': persons,
        'current_page': 'persons',
        'sort_criteria': request.GET.get('orderby')
    })
    return HttpResponse(t.render(c))

def person(request, person_id):
    person = Person.objects.get(pk=person_id)
    projects = Project.objects.filter(members__id=person_id)
    publications = Publication.objects.filter(authors__id=person_id)
    t = loader.get_template('Mperson.html')
    c = RequestContext(request,{
        'person': person,
        'projects': projects,
        'publications': publications,
        'current_page': 'persons'
    })
    return HttpResponse(t.render(c))

