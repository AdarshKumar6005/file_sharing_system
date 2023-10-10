from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.FileList.as_view(), name='filelist'),
    path('<int:pk>/', views.FileDownload.as_view(), name='filelist')
]