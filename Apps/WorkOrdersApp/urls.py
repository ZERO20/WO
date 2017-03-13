from django.conf.urls import include, url
from .views import DropZoneExample

urlpatterns = [
    url(r'^dropzone/$', DropZoneExample.as_view(), name='dropzone'),
]