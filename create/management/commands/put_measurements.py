import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from create.models import Measurements


class Command(BaseCommand):

    def handle(self, *args, **options):
        """ Read measurements """
        # Setup
        info = []
        fields = ['osm_id', 'value']
        # Reset table
        all = Measurements.objects.all()
        all.delete()
        # Read file content
        f = open(os.path.join(settings.RESOURCES, 'output.txt'), 'r')
        content = f.read()
        f.close()
        # Split into rows
        rows = content.split("\n")
        for row in rows:
            parts = row.split("|")
            try: tmp = {'osm_id': parts[0], 'value': parts[1]}
            except: continue
            info.append(tmp)
        # Write to database
        for inf in info:
            item = Measurements(**inf)
            item.save()
            
        
        