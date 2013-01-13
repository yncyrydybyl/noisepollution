import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from request.file_output import FileOutput

class Command(BaseCommand):

    def handle(self, *args, **options):
        csv = FileOutput()
        data = csv.get()
        f = open(os.path.join(settings.RESOURCES, 'polygons6.csv'), 'w')
        f.write(data)
        f.close()