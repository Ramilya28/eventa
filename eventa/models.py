from django.db import models

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
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='planned')  # новое поле

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
