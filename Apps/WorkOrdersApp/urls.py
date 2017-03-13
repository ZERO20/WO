from django.conf.urls import include, url
from .views import DropZoneExample, WorkOrdersListView, NewOrderView

urlpatterns = [
    url(r'^dropzone/$', DropZoneExample.as_view(), name='dropzone'),
    url(r'^work/orders/$', WorkOrdersListView.as_view(), name='work-orders-list'),
    url(r'^new/order/$', NewOrderView.as_view(), name='new-order'),
]