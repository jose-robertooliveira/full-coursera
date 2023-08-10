from django.contrib import admin
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from crud import views

# router = DefaultRouter()
# router.register(r"user", views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud/', include('crud.urls')),
]
