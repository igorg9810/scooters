from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'predictor'
urlpatterns = [
    path('', views.index, name='index'),
	path('post_new/', views.post_new, name='post_new'),
	path('post_new/train/', views.train, name='train'),
]