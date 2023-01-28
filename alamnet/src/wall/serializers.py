from rest_framework import serializers

from ..ViewSets.serializers import RecursiveSerializer, FilterCommentListSerializer
from .models import *

class CreateCommentSerializer(serializers.ModelSerializer):
    """ Add comment to post """
    class Meta:
        model = Comment
        fields = ('post', 'text', 'parent')

class ListCommentSerializer(serializers.ModelSerializer):
    """ Comments list """
    text = serializers.SerializerMethodField()
    children = RecursiveSerializer(many=True)
    user = serializers.ReadOnlyField(source='user.username')
    # deleted = serializers.BooleanField(default=False)

    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("id", "post", "user", "text", "created_date", "updated_date", "deleted", "children")

class PostSerializer(serializers.ModelSerializer):
    """ Display and redaction the post """
    user = serializers.ReadOnlyField(source='user.username')
    comments = ListCommentSerializer(many=True, read_only=True)
    view_count = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = ("id", "create_date", "user", "text", "comments", "view_count")

class ListPostSerializer(serializers.ModelSerializer):
    """ Posts list """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ("id", "create_date", "user", "text", "comments_count")


