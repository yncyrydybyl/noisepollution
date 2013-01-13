import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from request.decibels import NoiseMeasure

class Command(BaseCommand):

    def handle(self, *args, **options):
        lat = 
        lng = 0
        manager = NoiseMeasure(lat, lng)
        print manager.get()