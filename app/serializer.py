from rest_framework import serializers
from .models import Risk

class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = ['id', 'global_function', 'risk_topic', 'risk_response', 'risk_classification', 'risk_type', 'impact_classification',
                  'risk_appetite', 'description', 'status', 'action', 'monitoring']