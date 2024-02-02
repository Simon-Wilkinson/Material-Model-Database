
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
        files = os.listdir(settings.STATIC_ROOT)
        for file in files:
            if file.endswith('.json'):
                with open(os.path.join(settings.STATIC_ROOT, file)) as f:
                    data = json.load(f)
                    try:
                        Material.objects.create(name=data['name'], properties=data['properties'])
                        print(f"Loaded material {data['name']} from {file}")
                    except:
                        print(f"{file} does not contain a valid material data")