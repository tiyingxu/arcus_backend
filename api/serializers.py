from rest_framework import serializers
from api.models import Post, Translation

class PostSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(required=False, allow_null=True, use_url=False)

    class Meta:
        model = Post
        fields = ('id', 'picture', 'timestamp')

class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ('id', 'from_lang', 'from_word', 'other_word', 'other_lang', 'post')