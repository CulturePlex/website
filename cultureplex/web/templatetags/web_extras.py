from django import template
from web.models import Project

register = template.Library()

def carousel(value, arg):
    projects_list = Project.objects.filter(image__gt='').filter(incarousel=True)
    return projects_list

def truncatewords_by_chars(value, arg):
    """Truncate the text when it exceeds a certain number of characters.
    Delete the last word only if partial.
    Adds '...' at the end of the text.
    
    Example:
    
        {{ text|truncatewords_by_chars:25 }}
    """
    try:
        length = int(arg)
    except ValueError:
        return value
    
    if len(value) > length:
        if value[length:length + 1].isspace():
            return value[:length].rstrip() + '...'
        else:
            return value[:length].rsplit(' ', 1)[0].rstrip() + '...'
    else:
        return value

def show_person_box(person,width):
    return {'person': person,
            'width':width}

register.filter('carousel', carousel)
register.filter('truncatewords_by_chars', truncatewords_by_chars)
register.inclusion_tag('person_box.html')(show_person_box)
