from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('w1sales.urls')),
    path('w1sales/', include(('w1sales.urls','w1sales'),namespace='w1sales')),
    #path('contacts/', include(('contacts.urls','contacts'),namespace='contacts')),
    path('favicon.ico', RedirectView.as_view(url='/staticfiles/favico/favicon.ico')),
    path('captcha/', include('captcha.urls')),
]
