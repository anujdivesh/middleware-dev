from django.urls import path, include
from . import views
from .views import SubMenu2View  
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'submenu_2', SubMenu2View)

urlpatterns = [
    path('', include(router.urls)),

]
