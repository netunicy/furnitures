from django.urls import path
from django.conf.urls.static import static
from .import views
#from .views import PostView
#from .views import ArticlesDetailsView
from .import views

urlpatterns = [
    path('',views.homepage, name='w1sales'),
    path('about_us/',views.about_us, name='about_us'),
    path('services/',views.services, name='services'),
    path('contact_us/',views.contact_us, name='contact_us'),
]