from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(blank=True, null=True)
    participants = models.ManyToManyField(Participant, related_name='meetings')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date', 'time']