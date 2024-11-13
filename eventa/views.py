from rest_framework import viewsets
from .models import MeetingFile, Participant, Meeting
from .serializers import ParticipantSerializer, MeetingSerializer, MeetingResponseSerializer
from rest_framework.decorators import action


from django.core.mail import send_mail
from django.conf import settings

from rest_framework import viewsets
from .models import MeetingResponse

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

# class MeetingViewSet(viewsets.ModelViewSet):
#     queryset = Meeting.objects.all()
#     serializer_class = MeetingSerializer

#     def perform_create(self, serializer):
#         meeting = serializer.save()
#         files = self.request.FILES.getlist('files')  # Получаем файлы из запроса
#         for file in files:
#             MeetingFile.objects.create(meeting=meeting, file=file)  # Создаем объект MeetingFile для каждого файла


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def perform_create(self, serializer):
        meeting = serializer.save()
        files = self.request.FILES.getlist('files')
        for file in files:
            MeetingFile.objects.create(meeting=meeting, file=file)

    @action(detail=True, methods=['post'])
    def respond(self, request, pk=None):
        meeting = self.get_object()
        participant_id = request.data.get('participant_id')
        response_choice = request.data.get('response')

        # Проверка на корректность данных
        if not participant_id or response_choice not in dict(MeetingResponse.RESPONSE_CHOICES):
            return Response({"error": "Неверные данные"}, status=status.HTTP_400_BAD_REQUEST)

        # Поиск участника
        try:
            participant = Participant.objects.get(id=participant_id)
        except Participant.DoesNotExist:
            return Response({"error": "Участник не найден"}, status=status.HTTP_404_NOT_FOUND)

        # Создание или обновление отклика
        response, created = MeetingResponse.objects.update_or_create(
            meeting=meeting,
            participant=participant,
            defaults={'response': response_choice}
        )
        
        response_serializer = MeetingResponseSerializer(response)
        return Response(response_serializer.data, status=status.HTTP_200_OK)
    

class MeetingResponseViewSet(viewsets.ModelViewSet):
    queryset = MeetingResponse.objects.all()
    serializer_class = MeetingResponseSerializer

    



# class NotificationService:
#     @staticmethod
#     def send_notification(meeting, user, message):
#         # Создаем уведомление
#         notification = Notification.objects.create(
#             meeting=meeting,
#             user=user,
#             message=message
#         )
        
#         # Отправка email-уведомления
#         send_mail(
#             subject=f"Уведомление о встрече: {meeting.title}",
#             message=message,
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[user.email],
#             fail_silently=False,
#         )


# eventa/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Meeting

class SuggestedMeetingsView(APIView):
    permission_classes = [IsAuthenticated]  # Убедитесь, что пользователь аутентифицирован

    def get(self, request):
        user = request.user  # Получаем текущего аутентифицированного пользователя
        # Предполагаем, что у вас есть связь между участниками и встречами
        suggested_meetings = Meeting.objects.filter(participants=user)  # Получаем встречи, в которых участвует пользователь

        # Здесь вы можете сериализовать данные
        meetings_data = [
            {
                'id': meeting.id,
                'title': meeting.title,
                'date': meeting.date,
                'time': meeting.time,
                'description': meeting.description,
            }
            for meeting in suggested_meetings
        ]

        return Response(meetings_data)
