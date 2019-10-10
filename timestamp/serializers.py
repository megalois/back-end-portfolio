
from rest_framework import serializers
from timestamp.models import Timestamp

class TimestampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timestamp
        fields = ('unix_ts', 'date_ts')
        
        