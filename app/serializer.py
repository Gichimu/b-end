from rest_framework import serializers
from .models import Agent, Company, Property

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('id', 'fname', 'lname', 'email', 'phone', 'about_me')

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'title', 'transaction_type', 'price', 'bedrooms', 'bathrooms', 'location', 'description', 'bookmarked', 'agent')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('title', 'location')