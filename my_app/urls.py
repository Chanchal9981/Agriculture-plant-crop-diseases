from django.urls import path
from.import views

urlpatterns = [





    path('',views.Home),
    path('result',views.result,name='result')
]
