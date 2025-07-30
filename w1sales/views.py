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
    mylogo_home='https://res.cloudinary.com/htyiufnla/image/upload/v1753800919/ChatGPT_Image_Jul_29_2025_05_54_59_PM_f9dtol.png'
    new_key = CaptchaStore.generate_key()
    captcha_url = captcha_image_url(new_key)
    context = {
      'mylogo':mylogo_home,
      'captcha_url': captcha_url,
      'captcha_key': new_key,
       }
    if request.method == 'POST':
        captcha_key = request.POST.get('captcha_0')
        captcha_value = request.POST.get('captcha_1')

        try:
            store = CaptchaStore.objects.get(hashkey=captcha_key)
            if store.response != captcha_value.lower():
                # Wrong captcha
                new_key = CaptchaStore.generate_key()
                return render(request, 'w1sales/contact_us.html', {
                    'error': 'Invalid captcha. Please try again.',
                    'captcha_url': captcha_image_url(new_key),
                    'captcha_key': new_key,
                    'mylogo': mylogo_home
                })
        except CaptchaStore.DoesNotExist:
            new_key = CaptchaStore.generate_key()
            return render(request, 'w1sales/contact_us.html', {
                'error': 'Captcha expired or invalid.',
                'captcha_url': captcha_image_url(new_key),
                'captcha_key': new_key,
                'mylogo': mylogo_home
            })
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        full_message = f"""
        Name: {first_name}
        Surname: {last_name}
        Phone: {phone}
        Email: {email}

        Message:
        {message}
        """

        mail = mt.Mail(
            sender=mt.Address(email="hello@w1services.com", name="W1 Services Contact Form"),
            to=[mt.Address(email="frontofficew1services@gmail.com")],
            subject=subject,
            text=full_message,
            category="Contact from Website",
        )

        client = mt.MailtrapClient(token=MAILTRAP_API_TOKEN)
        client.send(mail)

        messages.add_message(request, messages.INFO, 'Your order was sent successfully. \nOne of our representatives will contact you as soon as possible.')
        return redirect('w1sales')

    return render(request, 'w1sales/contact_us.html',context)
