from django import template

register = template.Library()

def test(value, arg):
    return 'aqui va a ir el carusel de proyectos'

register.filter('test', test)
