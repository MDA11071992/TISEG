from django.conf.urls import url
from rest_framework.authtoken import views
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import *


urlpatterns = [
    url(r'^route/$', ViewRoute.as_view(), name='route'),
    url(r'^route/(?P<route_id>[0-9]+)/?$', ViewCoordinatesOnRoute.as_view(), name='coordinates'),
    url(r'^api-token-auth/', views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
