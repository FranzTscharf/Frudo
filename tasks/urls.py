from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.NewTaskView.as_view(), name='create'),
    path('newlabel/', views.NewLabelView.as_view(), name='newlabel'),
]