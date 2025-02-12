
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path("",include('userdata.urls')),
    path('admin/', admin.site.urls),
    path('userdata/', include('userdata.urls')),
    
]
