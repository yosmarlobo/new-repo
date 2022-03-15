from rest_framework import serializers

from apps.accounts.models import User


class UserCustomSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'date_joined'
        ]
