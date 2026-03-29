from rest_framework import serializers
from .models import Member, Contribution, Stokvel, Payout


class StokvelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stokvel
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = '__all__'


class PayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payout
        fields = '__all__'
