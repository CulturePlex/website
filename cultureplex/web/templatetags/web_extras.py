from django import template
from web.models import Project

register = template.Library()

def test(value, arg):
    code = "<div class='scrolli-element row'>"
    code += "<div class='span9'>"
    code += "          <img src='{{ STATIC_URL }}web/images/content/sample-02.png' />"
    code += "        </div>"
    code += "        <div class='span6'>"
    code += "          <h2>Titssulo del proyecto</h2>"
    code += "          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed et ornare risus. Cras vitae dui diam, et tincidunt libero. Integer eros ligula, ultricies eget consequat non, adipiscing eget odio.</p>"

    code += "          <p>Curabitur rutrum, augue a lacinia faucibus, metus enim consectetur ante, quis fermentum lacus dolor a tellus.</p>"
    code += "          <p><a class='btn primary'>Ver proyecto &raquo;</a></p>"
    code += "        </div>"
    code += "      </div><!-- .scrolli-element -->"
    projects_list = Project.objects.filter(image__gt='').filter(incarousel=True)
    return projects_list

register.filter('test', test)
