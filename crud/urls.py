from django.urls import path
# from .views import crud_view
from . import views

urlpatterns = [
    path('', views.mixin_view),
]
