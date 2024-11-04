# Generated by Django 5.1.2 on 2024-11-03 17:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='status',
            field=models.CharField(choices=[('planned', 'Планируемая'), ('completed', 'Завершенная'), ('canceled', 'Отмененная')], default='planned', max_length=10),
        ),
        migrations.CreateModel(
            name='MeetingFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='meeting_files/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='eventa.meeting')),
            ],
        ),
    ]
