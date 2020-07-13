from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    # url(r'properties/', views.properties, name='properties'),
    url(r'^api/agents/$', views.AgentList.as_view()),
    url(r'^api-token-auth/$', obtain_auth_token),
    url(r'api/agents/agent-id/(?P<pk>[0-9]+)/$', views.AgentDesc.as_view()),
    url(r'^api/properties/$', views.PropertyList.as_view()),
    url(r'^api/properties/property-id/(?P<pk>[0-9]+)/$', views.PropertyDesc.as_view()),
]
