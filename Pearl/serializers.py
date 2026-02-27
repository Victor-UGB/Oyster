from rest_framework import serializers
from .models import User,UserProfile, AbstractUser, Post, Tag, Folder
from .validators import validate_file_size
try:
    import magic
except Exception:
    magic = None
import mimetypes


class UserSerializers(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = ['id', 'created_at', 'updated_at', 'groups', 'user_permissions', 'username',]


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class RegisterUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True, min_length=6)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class PasswordResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = "__all__"
        extra_kwargs = {
            "pearl_image": {
                "validators": [validate_file_size(5 * 1024 * 1024, "Image")]
            },
            "pearl_audio": {
                "validators": [validate_file_size(10 * 1024 * 1024, "Audio")]
            },
            "pearl_video": {
                "validators": [validate_file_size(40 * 1024 * 1024, "Video")]
            },
        }
    
    def validate_pearl_image(self, value):
        return self.validate_file_type(value, ["image/jpeg", "image/png"])
    
    def validate_pearl_audio(self, value):
        return self.validate_file_type(value, ["audio/mpeg", "audio/wav"])
    
    def validate_pearl_video(self, value):
        return self.validate_file_type(value, ["video/mp4"])
    
    def validate_file_type(self, file, allowed_types):
        if not file:
            return file

        mime = None
        if magic is not None:
            try:
                mime = magic.from_buffer(file.read(2048), mime=True)
                file.seek(0)
            except Exception:
                mime = None

        if not mime:
            mime = getattr(file, 'content_type', None)

        if not mime:
            try:
                mime, _ = mimetypes.guess_type(getattr(file, 'name', '') or '')
            except Exception:
                mime = None

        if not mime or mime not in allowed_types:
            raise serializers.ValidationError(f'unsupported file type {mime}')

        return file
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"

class UserFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"



class ContentContextSerializer(serializers.ModelSerializer):
    pearl_image = serializers.FileField(required=False, allow_null = True, validators = [validate_file_size(5 * 1024 * 1024, "Image")])
    pearl_audio = serializers.FileField(required=False, allow_null = True, validators = [validate_file_size(10 * 1024 * 1024, "Audio")])
    pearl_video = serializers.FileField(required=False, allow_null = True, validators = [validate_file_size(40 * 1024 * 1024, "Video")])
    
    class Meta: 
        model = Post
        fields = ["pearl_image", "pearl_audio", "pearl_video"]
        extra_kwargs = {
            "pearl_image": {"write_only": True},
            "pearl_audio": {"write_only": True},
            "pearl_video": {"write_only": True},
        }