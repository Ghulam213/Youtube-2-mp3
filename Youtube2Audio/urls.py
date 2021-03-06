from django.urls import path
from . import views

app_name = "Youtube2Audio"

urlpatterns = [
    path('', views.index, name="index"),
    path("thankyou", views.thankYou, name="thankYou"),
    path('download', views.download, name="download"),
]
