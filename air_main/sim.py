# -*- coding: utf-8 -*-

#simpy
from __future__ import print_function
import simpy, random


'''


def car(env):
    while True:
        print 'Start parking at %d' % env.now
        parking_duration = 5
        yield env.timeout(parking_duration)
        print 'Start driving at %d' % env.now
        trip_duration = 2
        yield env.timeout(trip_duration)

# import simpy
env = simpy.Environment()
env.process(car(env))
env.run(until=100)

# print 'some text'

'''

class Plain(object):
    def __init__(self, env):
        self.env = env
        self.action = env.rocess(self.run())

    def run(self):
        while True:
            print('some')


            env = simpy.Enviroment()
            plain = Plain
            env