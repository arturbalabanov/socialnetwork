from rest_framework import serializers

from users.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile

        exclude = ('password', 'friends',)  # FIXME: friends should not be excluded, use the depth option for that
