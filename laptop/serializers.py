from rest_framework import serializers
from .models import UserInfo, Laptop, DamagedUnit


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ['id', 'name', 'email', 'contact_number', 'added_at', 'updated_at']

    """assumming that only PH +63 is used for contact number"""
    def validate_contact_number(self, value):
        if not value.isnumeric():
            raise serializers.ValidationError("contact number must contains numeric value (0-9)")
        if not len(value) == 11:
            raise serializers.ValidationError("invalid number, must contains 11 digits (09xxxxxxxxx)")
        return value
    
class LaptopSerializer(serializers.ModelSerializer):

    """assumming that serial number and order number can contain numeric and non-numeric values"""
    class Meta:
        model = Laptop
        fields = ['id', 'brand', 'model', 'serial_number', 'PO_number', 'status', 'current_user', 'added_at', 'updated_at']

    def validate(self, data):
        if len(data['brand']) < 2:
            raise serializers.ValidationError(
                {"brand":["invalid brand name, '{}' is less than 2 characters".format(data['brand'])]}
                )
        if len(data['model']) < 3:
            raise serializers.ValidationError(
                {"model":["invalid model name, '{}' is less than 3 characters".format(data['model'])]}
                )
        return data


class LaptopSummarySerializer(serializers.ModelSerializer):
    current_user_name = serializers.SerializerMethodField()

    def get_current_user_name(self, obj):
        if obj.current_user:
            return obj.current_user.name
        return None
    
    class Meta:
        model = Laptop
        fields = ['model', 'status', 'current_user_name']


class LaptopDetailedViewSerializer(serializers.ModelSerializer):
    current_user = UserInfoSerializer()

    class Meta:
        model = Laptop
        fields = ['id', 'brand', 'model', 'serial_number', 'PO_number', 'status', 'current_user']


class LaptopStatusSerializer(serializers.ModelSerializer):
    """ensures that laptop status is ONLY updated"""
    class Meta:
        model = Laptop
        fields = ['status']
    
    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


class LaptopCurrentUserSerializer(serializers.ModelSerializer):
    """ ensures that laptop's current user is only updated.
        assumed that current user can only have ONE laptop, raise error when trying to add 
        the same current user to other laptop. """
    class Meta:
        model = Laptop
        fields = ['current_user']

    def update(self, instance, validated_data):
        current_user = validated_data.get('current_user', instance.current_user)

        if current_user is not None and Laptop.objects.filter(current_user=current_user).exists():
            raise serializers.ValidationError("this user was already assigned to other laptop")
        
        instance.current_user = current_user
        instance.save()
        return instance


class DamagedUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = DamagedUnit
        fields = ['id', 'user', 'laptop', 'damage_type', 'description', 'added_at', 'updated_at']