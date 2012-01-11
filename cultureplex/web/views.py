from django.template import Context, loader
from web.models import Project
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Esta es la web del lab. <a href")

def projects(request):
    projects_list = Project.objects.all()
    t = loader.get_template('projects.html')
    c = Context({
        'projects_list': projects_list,
    })
    return HttpResponse(t.render(c))

def project(request, project_id):
    return HttpResponse("You're looking at project %s." % project_id)

