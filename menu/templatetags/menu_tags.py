from django import template
from ..models import MenuItem, Menu 

register = template.Library()



@register.simple_tag()
#@register.assignment_tag
def get_menu(slug):
    try :
    	mm = Menu.objects.get(slug=slug)
    	return mm
    except Exception as err :
    	return "nullpart"
     
