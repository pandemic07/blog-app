# # users/serializers.py
# from django.contrib.auth import get_user_model
# from rest_framework import serializers
# from .models import User

# # User = get_user_model()

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'name', 'email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_active')



from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password) # passwrd hash ho rha
        instance.save()
        return instance