
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParticipantViewSet, MeetingViewSet

router = DefaultRouter()
router.register(r'participants', ParticipantViewSet)
router.register(r'meetings', MeetingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
