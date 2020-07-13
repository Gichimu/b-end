from django.shortcuts import render, Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Agent, Company, Property
from .serializer import AgentSerializer, PropertySerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def home(request):
    return render(request, 'index.html')

# def properties(request):
#     return render(request, 'property.html')

class AgentList(APIView):
    def get(self, request, format=None):
        all_agents = Agent.objects.all()
        serializers = AgentSerializer(all_agents, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = AgentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (IsAuthenticated,)

class AgentDesc(APIView):
    permission_classes = (IsAuthenticated,)
    def get_agents(self, pk):
        try:
            return Agent.objects.get(pk=pk)
        except Agent.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        agent = self.get_agents(pk)
        serializers = AgentSerializer(agent)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        agent = self.get_agents(pk)
        serializers = AgentSerializer(agent, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        agent = self.get_agents(pk)
        agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PropertyList(APIView):
    def get(self, request, format=None):
        properties = Property.objects.all()
        serializers = PropertySerializer(properties, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = PropertySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    permission_classes = (IsAuthenticated,)

class PropertyDesc(APIView):
    permission_classes = (IsAuthenticated,)

    def get_properties(self, pk):
        try:
            return Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        props = self.get_properties(pk)
        serializers = PropertySerializer(props)
        return Response(serializers.data)
            
       

    def put(self, request, pk, format=None):
        prop = self.get_properties(pk)
        serializers = PropertySerializer(prop, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        prop = self.get_properties(pk)
        prop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
