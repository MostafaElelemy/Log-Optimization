from rest_framework import serializers
from .models import LogStream

class LogStreamSerializer(serializers.ModelSerializer):
    reduction_percentage = serializers.SerializerMethodField()

    class Meta:
        model = LogStream
        fields = ['id', 'source', 'raw_content', 'compressed_content', 'original_size', 'compressed_size', 'reduction_percentage', 'created_at']

    def get_reduction_percentage(self, obj):
        if obj.original_size > 0:
            reduction = ((obj.original_size - obj.compressed_size) / obj.original_size) * 100
            return round(reduction, 2)
        return 0