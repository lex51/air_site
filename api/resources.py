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
'''
from tastypie.throttle import CacheThrottle
from django.conf.urls import *
from tastypie.utils import trailing_slash


class PlainsResource(Resource):
    class Meta:
        allowed_methods = ['get']
        resource_name = 'plains'
        throttle = CacheThrottle()
        queryset = Plains.objects.all()


    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/search%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_search'), name="api_get_search"),
        ]

    def search(self, request, **kwargs):
        self.method_check(request, allowed=self.Meta.allowed_methods)
        self.is_authenticated(request)
        self.throttle_check(request)
        self.log_throttled_access(request)

        # Do the query.
        sqs = SearchQuerySet().models(Plains).load_all().auto_query(request.GET.get('q', ''))
        paginator = Paginator(sqs, 20)

        try:
            page = paginator.page(int(request.GET.get('page', 1)))
        except InvalidPage:
            raise Http404("Sorry, no results on that page.")

        objects = []

        for result in page.object_list:
            bundle = self.build_bundle(obj=result.object, request=request)
            bundle = self.full_dehydrate(bundle)
            objects.append(bundle)

        object_list = {
            'objects': objects,
        }

        return self.create_response(request, object_list)
'''