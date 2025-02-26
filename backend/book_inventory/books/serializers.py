from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User
from django.utils.timezone import now, timedelta
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken
from .models import OTP
from django.contrib.auth import get_user_model


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model: User
        fields = ["id", "username", "email"]


User = get_user_model()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        # find the user by email
        user = User.objects.filter(email=email).first()
        if not user or not user.check_password(password):
            raise serializers.ValidationError("Invalid credentials")
        # Generate OTP
        otp_code = OTP.generate_otp()
        OTP.objects.update_or_create(
            user=user,
            defaults={"code": otp_code, "expires_at": now() + timedelta(minutes=5)},
        )

        send_mail(
            "Your OTP Code",
            f"Your OTP is {otp_code}.It expires in 5 minutes",
            "",
            [user.email],
            fail_silently=False,
        )

        return {"message": "OTP sent successfully", "email": user.email}


class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        user = User.objects.filter(email=data["email"]).first()
        if not user:
            raise serializers.ValidationError("User not found")

        otp = OTP.objects.filter(user=user, code=data["code"]).first()
        if not otp or otp.is_expired():
            raise serializers.ValidationError("Invalid or expired OTP")

        otp.delete()
        refresh = RefreshToken.for_user(user)
        return {"access": str(refresh.access_token), "refresh": str(refresh)}
