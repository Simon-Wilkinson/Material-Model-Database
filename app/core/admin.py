from django.contrib import admin

admin.site.site_header = 'AniForm Material Database Administration'

# register material model
from core.models import Material, Characterisation, Experiment, MaterialMechanismModel, MaterialModel
admin.site.register(Material)
admin.site.register(Characterisation)
admin.site.register(Experiment)
admin.site.register(MaterialMechanismModel)
admin.site.register(MaterialModel)


