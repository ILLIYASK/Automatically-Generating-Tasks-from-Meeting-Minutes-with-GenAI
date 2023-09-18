from django.urls import path
from . import  views

urlpatterns = [
    path('',views.main,name='main_page'),
    path('upload/', views.upload, name='upload_page'),
    path('table/', views.table, name='table_page'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('download-excel/', views.download_excel, name='download_excel'),


]