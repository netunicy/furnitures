from django.conf.urls.static import static
from .import views
from django.urls import path
from django.conf import settings


urlpatterns = [
    path('',views.homepage, name='w1sales'),
    path('about_us/',views.about_us, name='about_us'),
    path('services/',views.services, name='services'),
    path('contact_us/',views.contact_us, name='contact_us'),
    path('our_products/',views.our_products, name='our_products'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)