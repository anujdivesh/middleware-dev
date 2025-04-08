from django.urls import path, include
from . import views
from .views import ProjectView  
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'project', ProjectView)

urlpatterns = [
    path('', include(router.urls)),

]
