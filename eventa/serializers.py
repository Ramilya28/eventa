from rest_framework import serializers
from .models import Participant, Meeting, MeetingResponse

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

# class MeetingSerializer(serializers.ModelSerializer):
#     participants = serializers.PrimaryKeyRelatedField(
#         many=True,
#         queryset=Participant.objects.all()  
#     )
#     files = MeetingFileSerializer(many=True, required=False) 
#     class Meta:
#         model = Meeting
#         fields = '__all__'

class MeetingResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingResponse
        fields = '__all__'

class MeetingSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Participant.objects.all()
    )
    files = MeetingFileSerializer(many=True, required=False)
    responses = MeetingResponseSerializer(many=True, read_only=True)  # Новое поле для откликов

    class Meta:
        model = Meeting
        fields = '__all__'

