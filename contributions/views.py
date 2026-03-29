from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Member, Contribution, Stokvel, Payout
from .serializers import MemberSerializer, ContributionSerializer, StokvelSerializer, PayoutSerializer


class StokvelViewSet(viewsets.ModelViewSet):
    queryset = Stokvel.objects.all()
    serializer_class = StokvelSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    @action(detail=True, methods=['get'])
    def balance(self, request, pk=None):
        member = self.get_object()
        contributions = Contribution.objects.filter(member=member)
        total_contributed = sum(c.amount for c in contributions)
        missed = contributions.filter(status='missed').count()
        late = contributions.filter(status='late').count()
        paid = contributions.filter(status='paid').count()

        return Response({
            'member': member.name,
            'stokvel': member.stokvel.name if member.stokvel else None,
            'total_contributed': total_contributed,
            'paid_contributions': paid,
            'missed_contributions': missed,
            'late_contributions': late,
        })


class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer


class PayoutViewSet(viewsets.ModelViewSet):
    queryset = Payout.objects.all()
    serializer_class = PayoutSerializer
