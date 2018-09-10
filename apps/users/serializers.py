from rest_framework import serializers

from .models import User, PROFILES


class UserSerializer(serializers.ModelSerializer):
    """docstring for UserSerializer"""
    profile_name = serializers.ReadOnlyField(source='get_profile_display')
    profile = serializers.ChoiceField(PROFILES)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'name',
                  'username', 'email',
                  'profile', 'profile_name')
