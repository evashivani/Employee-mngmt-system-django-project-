from django.urls import URLPattern,path
from .views import *
urlpatterns=[
    path('emp/',view_employee)
]
