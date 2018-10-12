# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

@python_2_unicode_compatible
class AirPorts(models.Model):
    port_name = models.CharField(max_length=200)
    port_name_city = models.CharField(max_length=200, blank = True)

    def __str__(self):
        return self.port_name

@python_2_unicode_compatible
class Plains(models.Model):
    states = (
        ('on the way', 'в пути'),
        ('landed', 'приземлился'), 
        ('boarding ',  'посадка пассажиров'), 
        ('disembarking',  'высадка пассажиров'), 
        ('delay', 'задержан'), 
        )
    plain_name = models.CharField(max_length=200, blank = True)
    plain_no = models.IntegerField(blank = True, null = True)
    plain_discribe = models.CharField(max_length=200, blank = True)
    # current_aim = models.ForeignKey('AirPorts', max_length=200)
    plain_type = models.CharField(max_length=200, blank = True)
    plain_port_in = models.ForeignKey('AirPorts', max_length=200, blank = True, null = True, related_name = 'plain_port_in')
    plain_port_out = models.ForeignKey('AirPorts', max_length=200, blank = True, null = True, related_name = 'plain_port_out')
    plain_state = models.CharField(choices = states, max_length = 15, blank = True, null = True)#, blank = True )
    plain_time_left = models.IntegerField(blank = True, null = True)

    def __str__(self):
        return self.plain_name