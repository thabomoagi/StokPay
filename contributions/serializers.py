from rest_framework import serializers
from .models import Member, Contribution


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributionfields = '__all__'
