from django.urls import include, path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('api/', include('apps.tasks.api.urls')),
    path('', views.TaskView.as_view(), name='task')
]