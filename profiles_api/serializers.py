from rest_framework import serializers
from .models import UserProfile

class TestSerializer(serializers.Serializer):
    """Serializes a name field for testing APIView"""
    name = serializers.CharField(max_length=5)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializers user profile object"""

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only':True,
                'style': {'input_type': 'password'}
                # to make it *** when writing pass
            }
        }

    def create(self, validated_data):
        """Create and return new user"""

        user = UserProfile.objects.create_user(
            email = validated_data.get("email"),
            name = validated_data.get("name"),
            password = validated_data.get("password")
        )

        return user
