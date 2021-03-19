from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns

from api import views_sentiment

#from rest_framework_swagger.views import get_swagger_view
#schema_view = get_swagger_view(title='Text Categorization API')
from api import swagger
schema_view = swagger.schema_view


urlpatterns = [
    url(r'^api/master/sentimentAnalysisBM', views_sentiment.SentAnalysisMalay.as_view())
]

#urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns







