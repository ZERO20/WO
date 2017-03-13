#encoding:utf-8
from django.views.generic import TemplateView
from .models import  Order

class DropZoneExample(TemplateView):
    "Example of dropzone usage"
    template_name = 'drop_zone_example.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        print('the photo arrived!')
        return super(TemplateView, self).render_to_response(context)


class WorkOrdersListView(TemplateView):
    "Example of dropzone usage"
    template_name = 'work_orders_list.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        print('the photo arrived!')
        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(WorkOrdersListView, self).get_context_data(**kwargs)
        context['orders'] = Order.objects.all()
        context['list_orders'] = 'active'
        context['work_orders'] = 'active'
        return context