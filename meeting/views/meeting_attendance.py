from rest_framework import viewsets
from meeting.models import MeetingAttendance
from meeting.serializers import MeetingAttendanceSerializer


class MeetingAttendanceViewSet(viewsets.ModelViewSet):
    queryset = MeetingAttendance.objects.all()
    serializer_class = MeetingAttendanceSerializer