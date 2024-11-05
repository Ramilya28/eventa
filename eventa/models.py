from django.db import models
from django.forms import ValidationError

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Meeting(models.Model):
    STATUS_CHOICES = [
        ('planned', 'Планируемая'),
        ('completed', 'Завершенная'),
        ('canceled', 'Отмененная'),
    ]

    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(blank=True, null=True)
    participants = models.ManyToManyField(Participant, related_name='meetings')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='planned')

    def clean(self):
        # Валидация времени, чтобы оно не содержало секунд
        if self.time.second != 0:
            raise ValidationError('Время должно быть указано без секунд.')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date', 'time']

class MeetingFile(models.Model):
    meeting = models.ForeignKey(Meeting, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='meeting_files/')  # Папка для хранения файлов
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File for {self.meeting.title}"

class MeetingResponse(models.Model):
    RESPONSE_CHOICES = [
        ('agreed', 'Согласен'),
        ('canceled', 'Отменена'),
        ('rescheduled', 'Перенесена'),
    ]

    meeting = models.ForeignKey(Meeting, related_name='responses', on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, related_name='responses', on_delete=models.CASCADE)
    # response = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    response = models.CharField(max_length=11, choices=RESPONSE_CHOICES)
    responded_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('meeting', 'participant')  # Уникальное сочетание встречи и участника


# from django.db import models
from django.contrib.auth.models import User

# class Notification(models.Model):
#     meeting = models.ForeignKey('Meeting', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.TextField()
#     is_read = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
