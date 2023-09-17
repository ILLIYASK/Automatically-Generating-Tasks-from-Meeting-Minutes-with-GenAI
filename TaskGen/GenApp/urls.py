from django.urls import path
from . import  views

urlpatterns = [
    path('',views.main,name='main_page'),
    path('upload/', views.upload, name='upload_page'),
    path('table/', views.table, name='table_page'),
    path('edit_table/', views.edit_table, name='edit_page'),

]