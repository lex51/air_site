from tastypie.resources import ModelResource, Resource
from air_main.models import Plains

class PlainsResource(ModelResource):
    class Meta:
        queryset = Plains.objects.all()
        resource_name = 'plains'
        fields = ['plain_no', 'plain_port_in', 'plain_port_out', 'plain_state']
        filtering = {'plain_port_in':['id'],
                     'plain_port_out':['id'],
                     'plain_state':['icontains'],
                     }
