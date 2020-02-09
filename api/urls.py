from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import JournalViewSet


router = DefaultRouter()
router.register(r'Journals', JournalViewSet)
urlpatterns = router.urls





