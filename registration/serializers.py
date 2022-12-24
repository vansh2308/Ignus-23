from rest_framework import serializers, exceptions
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import UserProfile, PreRegistration
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

User = get_user_model()


class PreRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreRegistration
        fields = ["full_name", "email", "phone_number", "college", "college_state", "current_year", "por", "por_holder_contact"]


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': False}
        }


class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None

    def validate(self, attrs):
        attrs['refresh'] = self.context['request'].COOKIES.get('refresh')
        if attrs['refresh']:
            return super().validate(attrs)
        else:
            raise exceptions.ParseError(
                'No valid token found in cookie \'refresh\'')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email", "is_google", "profile_complete"]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["referred_by", "referred_by_igmun", "user", "phone", "gender", "current_year", "college", "state", "passes", "registration_code", "registration_code_igmun", "is_ca", "is_igmun_ca", "amount_paid", "amount_due", "qr_code"]
