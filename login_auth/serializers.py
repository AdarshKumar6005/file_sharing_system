from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegistrationSerializer(serializers.Serializer):
    password2=serializers.CharField()
    class Meta:
        model = User
        fields = ['username','email','password','first_name','last_name']

    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError('Password and Confirm Password should be same.')
        attrs.pop('password2')
        return attrs
    # def create(self, validate_data):
    #     return User.objects.create_user(**validate_data)