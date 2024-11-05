
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParticipantViewSet, MeetingViewSet, MeetingResponseViewSet, SuggestedMeetingsView

router = DefaultRouter()
router.register(r'participants', ParticipantViewSet)
router.register(r'meetings', MeetingViewSet)
router.register(r'responses', MeetingResponseViewSet) 

urlpatterns = [
    path('', include(router.urls)),
    path('api/suggested-meetings/', SuggestedMeetingsView.as_view(), name='suggested_meetings'),
]
