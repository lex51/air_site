# -*- coding: utf-8 -*- 
from air_main.models import Plains, AirPorts
from table import Table
from table.columns import Column

class PlainsTableIn(Table):
    # id = Column(field='id')
    # name = Column(field='plain_name', header = u'текст!!')
    no = Column(field='plain_no', header = u'номер рейса')
    plain_type = Column(field = 'plain_type', header = u'тип')
    plain_port_in = Column(field= 'plain_port_in',  header = u'пункт следования')
    plain_port_out = Column(field = 'plain_port_out', header = u'пункт отправки')
    plain_state = Column(field = 'plain_state', header  = u'статус')
    plain_time_left = Column( field = 'plain_time_left', header = u'времени осталось')

    class Meta:
        model = Plains
        # ajax = True
        pagination = False
        ext_button = True
        search = True
        zero_records = u'записи не найдены, сожалеем )'

class PlainsTableOut(Table):
    # id = Column(field='id')
    # name = Column(field='plain_name', header = u'текст!!')
    no = Column(field='plain_no', header = u'номер рейса')
    plain_type = Column(field = 'plain_type', header = u'тип')
    plain_port_in = Column(field= 'plain_port_in',  header = u'пункт следования')
    plain_port_out = Column(field = 'plain_port_out', header = u'пункт отправки')
    plain_state = Column(field = 'plain_state', header  = u'статус')
    plain_time_left = Column( field = 'plain_time_left', header = u'времени осталось')

    class Meta:
        model = Plains
        # ajax = True
        pagination = False
        ext_button = True
        search = True
        zero_records = u'записи не найдены, сожалеем )'