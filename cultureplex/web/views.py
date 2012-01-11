from django.template import Context, loader
from web.models import Project
from web.models import Publication
from web.models import People
from django.http import HttpResponse

def index(request):
    i = loader.get_template('index.html')
    c = Context({
    })
    return HttpResponse(i.render(c))

def projects(request):
    projects_list = Project.objects.all()
    t = loader.get_template('projects.html')
    c = Context({
        'projects_list': projects_list,
    })
    return HttpResponse(t.render(c))

def project(request, project_id):
    project = Project.objects.get(pk=project_id)
    t = loader.get_template('project.html')
    c = Context({
        'project': project,
    })
    return HttpResponse(t.render(c))

def publications(request):
    publications_list = Publication.objects.all()
    t = loader.get_template('publications.html')
    c = Context({
        'publications_list': publications_list,
    })
    return HttpResponse(t.render(c))

def publication(request, publication_id):
    publication = Publication.objects.get(pk=publication_id)
    t = loader.get_template('publication.html')
    c = Context({
        'publication': publication,
    })
    return HttpResponse(t.render(c))

def people_index(request):
    people_list = People.objects.all()
    t = loader.get_template('people_index.html')
    c = Context({
        'people_list': people_list,
    })
    return HttpResponse(t.render(c))

def people(request, people_id):
    people = People.objects.get(pk=people_id)
    t = loader.get_template('people.html')
    c = Context({
        'people': people,
    })
    return HttpResponse(t.render(c))



