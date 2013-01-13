import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from request.decibels import NoiseMeasure

class Command(BaseCommand):

    def handle(self, *args, **options):
        lat = 52.52645684487169 
        lng = 13.415439824006349
        manager = NoiseMeasure(lat, lng)
        print manager.get()