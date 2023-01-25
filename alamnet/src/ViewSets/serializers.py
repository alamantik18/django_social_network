from rest_framework import serializers

class FilterCommentListSerializer(serializers.ListSerializer):
    """ Filter for comments """
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)

class RecursiveSerializer(serializers.Serializer):
    """ Output comments for comment)) """
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data