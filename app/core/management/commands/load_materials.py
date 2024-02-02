
from django.core.management.base import BaseCommand
from django.conf import settings
from core.models import Material
import os
import json

class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):

        Material.objects.all().delete()
        """Entrypoint for command."""
        self.stdout.write('Loading materials...')

        files = os.listdir(os.path.join(settings.STATIC_ROOT, 'materials'))
        for file in files:
            with open(os.path.join(settings.STATIC_ROOT, 'materials', file)) as f:
                data = json.load(f)
                Material.objects.create(name=data['name'], properties=data['properties'])
            print(f"Loaded material {data['name']} from {file}")