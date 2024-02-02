from django.contrib import admin

admin.site.site_header = 'AniForm Material Database Administration'

# register material model
from core.models import Material
admin.site.register(Material)