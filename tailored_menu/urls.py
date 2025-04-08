from django.urls import path, include
from . import views
from .views import TailoredMenuView  
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tailored_menu', TailoredMenuView)

urlpatterns = [
    path('', include(router.urls)),

]
