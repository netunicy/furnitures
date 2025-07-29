from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def homepage(request):
  mylogo_home=''
  template = loader.get_template('main_page.html')
  context = {
    'mylogo':mylogo_home,
  }
  return HttpResponse(template.render(context, request))
