from django.shortcuts import render
from django.http import HttpResponse
from air_main.models import Plains, AirPorts
from django.template import loader
from tables import PlainsTableIn, PlainsTableOut

# Create your views here.
# def main_view(request):
    # return render('some_text')

def main_view(request):
    # return HttpResponse('some_text')
    # plane_list = Plains.objects.all()
    plane_list_in = Plains.objects.filter(plain_port_in=1)
    plane_list_out = Plains.objects.filter(plain_port_out=1)
    templ = loader.get_template('main.html')
    # return HttpResponse(templ.render(plane_list, request))
    return render(request,
     'main.html',
     # 'test.html', 
      {'plane_list_in': plane_list_in, 'plane_list_out': plane_list_out})

def test_table(request):
    plane_in = PlainsTableIn(Plains.objects.filter(plain_port_in=1))
    plane_out = PlainsTableOut(Plains.objects.filter(plain_port_out=1))
    return render(request, 'index.html', {'plane_in':plane_in, 'plane_out': plane_out})