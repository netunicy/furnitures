from django.urls import path
from django.conf.urls.static import static
from .import views
#from .views import PostView
#from .views import ArticlesDetailsView
from .import views

urlpatterns = [
    path('',views.homepage, name='w1sales'),

]