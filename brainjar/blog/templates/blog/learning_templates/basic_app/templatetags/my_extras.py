from django import template

register = template.Library()

@register.filter(name='chop')
def chop(value,arg):
    """
    This cuts out all values of arg from the string.
    """
    return value.replace(arg,'')
# REGISTER THE FUCNTION
# NAME, FUNCTION
