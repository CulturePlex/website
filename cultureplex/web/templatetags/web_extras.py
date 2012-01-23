from django import template
from web.models import Project

register = template.Library()

def test(value, arg):
    projects_list = Project.objects.filter(incarousel=True)
    return projects_list

register.filter('test', test)
