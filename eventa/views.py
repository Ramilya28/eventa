from rest_framework import viewsets
from .models import MeetingFile, Participant, Meeting
from .serializers import ParticipantSerializer, MeetingSerializer

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def perform_create(self, serializer):
        meeting = serializer.save()
        files = self.request.FILES.getlist('files')  # Получаем файлы из запроса
        for file in files:
            MeetingFile.objects.create(meeting=meeting, file=file)  # Создаем объект MeetingFile для каждого файла

