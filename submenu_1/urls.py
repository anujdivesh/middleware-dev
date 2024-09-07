from django.urls import path, include
from . import views
from .views import SubMenu1View  
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'submenu_1', SubMenu1View)

urlpatterns = [
    path('', include(router.urls)),

]
