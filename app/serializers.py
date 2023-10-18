from django.contrib.auth import get_user_model
from rest_framework import serializers, fields
from rest_framework.exceptions import ValidationError
from app.models import Comment, Posts

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class PostSerializer(serializers.ModelSerializer):
    author = fields.HiddenField(default=fields.CurrentUserDefault())

    class Meta:
        model = Posts
        fields = ('title', 'author', 'description')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['author'] = UserSerializer(instance.author).data
        return repr


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ()


class FormSerializers(serializers.Serializer):
    image = fields.ImageField(required=False)
    name = fields.CharField(max_length=255)
    address = fields.CharField(max_length=255, min_length=10, allow_blank=True)
    phone = fields.CharField(max_length=55, required=False)
    email = fields.EmailField(max_length=55, write_only=True)

    def validate_name(self, value):
        if not value.isalpha():
            raise ValidationError('only alphabet')
        return value

    def validate_phone(self, value):
        if not value.isnumeric():
            raise ValidationError('only digit')
        return value

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        return repr
