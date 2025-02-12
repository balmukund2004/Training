
from django.contrib import admin
from django.urls import path
from . import views
from .views import predict_fraud

urlpatterns = [
    path('tests/',views.home),
    # path('admin/', admin.site.urls),
    # path('', include('userdata.urls')),
    path('calc/',views.calculator),
    path('navbar/',views.navbar),
    path('',views.landingpage),
    path('userform/',views.userdata, name = 'userform'),
    path('fetchdata/',views.fetchdata,name='fetchdata'),
    path('predict_fraud/', views.predict_fraud, name='predict_fraud'),
    path('userdata/', views.userdata, name='userdata'),
    path('update_userdata/',views.update_userdata, name = 'update_userdata'),
    path('deleteuserdata/',views.deleteuserdata, name = 'deleteuserdata'),
]