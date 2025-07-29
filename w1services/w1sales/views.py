from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def homepage(request):
  mylogo_home='https://res.cloudinary.com/htyiufnla/image/upload/v1753800919/ChatGPT_Image_Jul_29_2025_05_54_59_PM_f9dtol.png'
  template = loader.get_template('main_page.html')
  context = {
    'mylogo':mylogo_home,
  }
  return HttpResponse(template.render(context, request))
