from rest_framework import viewsets
from members.models import Member
from members.serializers import MemberSerializer

class MemberViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
