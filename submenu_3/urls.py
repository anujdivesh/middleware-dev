from django.urls import path, include
from . import views
from .views import SubMenu3View  
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'submenu_3', SubMenu3View)

urlpatterns = [
    path('', include(router.urls)),

]
