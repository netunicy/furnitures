import os
from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
import mailtrap as mt
from django.shortcuts import render
import os
from django.contrib import messages
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from .forms import ContactForm

def homepage(request):
  mylogo_home='https://res.cloudinary.com/htyiufnla/image/upload/v1753800919/ChatGPT_Image_Jul_29_2025_05_54_59_PM_f9dtol.png'
  template = loader.get_template('main_page.html')
  context = {
    'mylogo':mylogo_home,
  }
  return HttpResponse(template.render(context, request))

def about_us(request):
  mylogo_home='https://res.cloudinary.com/htyiufnla/image/upload/v1753800919/ChatGPT_Image_Jul_29_2025_05_54_59_PM_f9dtol.png'
  template = loader.get_template('about_us.html')
  context = {
    'mylogo':mylogo_home,
  }
  return HttpResponse(template.render(context, request))

def services(request):
  mylogo_home='https://res.cloudinary.com/htyiufnla/image/upload/v1753800919/ChatGPT_Image_Jul_29_2025_05_54_59_PM_f9dtol.png'
  template = loader.get_template('services.html')
  context = {
    'mylogo':mylogo_home,
  }
  return HttpResponse(template.render(context, request))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, 'mailtrap_token.txt')) as f:
    MAILTRAP_API_TOKEN = f.read().strip()

def contact_us(request):
    mylogo_home = 'https://res.cloudinary.com/htyiufnla/image/upload/v1753800919/ChatGPT_Image_Jul_29_2025_05_54_59_PM_f9dtol.png'
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Retrieve form data
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            phone = form.cleaned_data.get('phone', 'N/A')
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            mail = mt.Mail(
                sender=mt.Address(email="hello@w1services.com", name="W1 Services Contact Form"),
                to=[mt.Address(email="frontofficew1services@gmail.com")],
                subject=subject,
                text=f"{name} {surname}\n{phone}\n{email}\n{message}",
                category="Contact from Website",
            )

            client = mt.MailtrapClient(token=MAILTRAP_API_TOKEN)
            client.send(mail)

            messages.add_message(request, messages.INFO, 
                'Your message has been successfully sent. One of our representatives will contact you shortly.'
            )
            return redirect('w1sales')

    # ✅ Common context for both GET and failed POST
    context = {
        'mylogo': mylogo_home,
        'form': form
    }
    return render(request, "contact_us_form.html", context)

                