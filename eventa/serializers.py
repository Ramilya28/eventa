from rest_framework import serializers
from .models import Participant, Meeting

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

from rest_framework import serializers
from .models import Participant, Meeting, MeetingFile

class MeetingFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingFile
        fields = '__all__'

class MeetingSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Participant.objects.all()  
    )
    files = MeetingFileSerializer(many=True, required=False)  # добавляем файлы

    class Meta:
        model = Meeting
        fields = '__all__'

