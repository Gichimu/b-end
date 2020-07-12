from rest_framework import serializers
from .models import Agent, Company, Property

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('id', 'fname', 'lname', 'email', 'phone', 'about_me')