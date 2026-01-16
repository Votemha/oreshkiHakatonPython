from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("notes/", views.note_list, name="note_list"),
    path("notes/create/", views.note_create, name="note_create"),
    path("notes/<int:pk>/edit/", views.note_edit, name="note_edit"),
    path("notes/<int:pk>/delete/", views.note_delete, name="note_delete"),

    path("users/", views.admin_user_list, name="admin_user_list"),
    path("users/create/", views.admin_user_create, name="admin_user_create"),
    path("users/<int:pk>/edit/", views.admin_user_edit, name="admin_user_edit"),
    path("users/<int:pk>/delete/", views.admin_user_delete, name="admin_user_delete"),
]
