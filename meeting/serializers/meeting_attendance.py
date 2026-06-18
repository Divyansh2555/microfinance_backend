from rest_framework import serializers
from meeting.models.meeting_attendance import MeetingAttendance


class MeetingAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingAttendance
        fields = '__all__'