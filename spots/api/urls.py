from django.urls import path
from spots.api import views

urlpatterns = [
    path('spots/',views.ListView.as_view(),name='list')
]
