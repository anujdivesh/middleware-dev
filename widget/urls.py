from django.urls import path, include
from . import views
from .views import WidgetView  
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'widget', WidgetView)

urlpatterns = [
    path('', include(router.urls)),

]
