from django.urls import path
from . import views


urlpatterns = [
    path("app/", views.index, name="index"),
    path("update/<int:pk>/", views.update_task, name="update_task"),
    path("delete/<int:pk>/", views.delete_task, name="delete_task")
]