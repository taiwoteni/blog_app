from django.urls import path
from . import views

urlpatterns = [
    path('post/<slug:slug>/comment/', views.add_comment, name='add-comment'),
]
