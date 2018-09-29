from rest_framework import serializers

from .models import User, PROFILES


class UserSerializer(serializers.ModelSerializer):
    """ User Serializer """
    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'},
                                     )
    profile_name = serializers.ReadOnlyField(source='get_profile_display')
    profile = serializers.ChoiceField(PROFILES)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'name', 'username',
                  'email', 'profile', 'profile_name', 'password',
                  )
        write_only_fields = ('password',)

    def create(self, validated_data):
        """ Override this method in order to set an usable password """
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
