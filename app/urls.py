from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('users/create/', views.user_create, name='user_create'),
    path('users/delete/<int:user_id>/', views.user_delete, name='user_delete'),

    path('notes/<int:user_id>/', views.notes_list, name='notes_list'),
    path('notes/create/<int:user_id>/', views.note_create, name='note_create'),
    path('notes/delete/<int:note_id>/', views.note_delete, name='note_delete'),
]