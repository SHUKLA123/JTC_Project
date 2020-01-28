from django import template

register = template.Library()

def line_remove(value):
    a = value[0:180]
    b = a+"..."

    return b

register.filter('lineremover',line_remove)

def time_loop(number):
    return range(number)

register.filter('times',time_loop)
