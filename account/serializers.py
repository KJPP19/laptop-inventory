from .models import CustomAccount, LogIn
from rest_framework import serializers


class CustomAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomAccount
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {'password': {'write_only':True}}

    def validate(self, data):
        if data['email']:
            if CustomAccount.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError("'{}' was already taken".format(data['email']))
        return data
    
    def create(self, validated_data):
        return CustomAccount.objects.create_user(**validated_data)


class LogInSerializer(serializers.ModelSerializer):

    class Meta:
        model = LogIn
        fields = ['email', 'password']