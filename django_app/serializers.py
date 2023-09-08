# not implemented yet
# will be used when creating a react frontend in converting to JSON objects

from rest_framework import serializers
from .models import UserProfile,Items

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        
class ItemsSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()  

    class Meta:
        model = Items
        fields = '__all__'

