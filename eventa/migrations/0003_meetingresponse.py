# Generated by Django 5.1.2 on 2024-11-04 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventa', '0002_meeting_status_meetingfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(choices=[('agreed', 'Согласен'), ('canceled', 'Отменена'), ('rescheduled', 'Перенесена')], max_length=11)),
                ('responded_at', models.DateTimeField(auto_now=True)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='eventa.meeting')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='eventa.participant')),
            ],
            options={
                'unique_together': {('meeting', 'participant')},
            },
        ),
    ]
