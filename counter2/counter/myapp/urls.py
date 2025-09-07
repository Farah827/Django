from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index ,name='index') ,
    path('destroy_session' , views.destroy_session , name='destroy_session'),
    path('increment2' ,views.increment2 , name='increment2'),
    path('increment_value' ,views.increment_value , name='increment_value') 
]