from django.urls import path, include
from .views import NoticeView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'notice', NoticeView)

urlpatterns = [
    path('', include(router.urls)),

]
