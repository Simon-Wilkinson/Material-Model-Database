from django.db import models

# Create your models here.

class Material(models.Model):
    """Material object"""
    name = models.CharField(max_length=100)
    description = models.TextField(default='No description', blank=True)
    supplier = models.CharField(max_length=100, null=True, blank=True)
    fibre_material = models.CharField(max_length=100, null=True, blank=True)
    matrix_material = models.CharField(max_length=100, null=True, blank=True)
    access = models.CharField(max_length=10, default='admin')

    def __str__(self):
        return self.name

class Characterisation(models.Model):
    date = models.DateField(null=True, blank=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=100, null=True, blank=True)
    access = models.CharField(max_length=10, default='admin')

    def __str__(self):
        return f"{self.material.name} - {self.date}"
        

class MechanismChoices(models.TextChoices):
    INPLANE = "Inplane", "Inplane"
    BENDING = "Bending", "Bending"
    INTERFACE = "Interface", "Interface"

class Experiment(models.Model):
    characterisation = models.ForeignKey(Characterisation, on_delete=models.CASCADE)
    mechanism = models.CharField(max_length=100, choices=MechanismChoices.choices)
    test_description = models.TextField(null=True, blank=True)
    test_data = models.JSONField(default=dict, blank=True)

    def __str__(self) :
        return f"{self.characterisation.material.name} - {self.mechanism}"

class MaterialMechanismModel(models.Model):
    experiments = models.ManyToManyField(Experiment, related_name='material_models')
    mechanism = models.CharField(max_length=100, choices=MechanismChoices.choices)
    fitting_configuration = models.JSONField(default=dict, blank=True)
    model = models.JSONField(default=dict, blank=True)

    def save(self, *args, **kwargs):
        # Ensure that the mechanism matches across the model and experiments
        if self.experiments.exists():
            mechanisms = self.experiments.values_list('mechanism', flat=True).distinct()
            if len(mechanisms) > 1 or mechanisms[0] != self.mechanism:
                raise ValueError("All associated experiments must have the same mechanism as the MaterialMechanismModel")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.mechanism + " model"

class MaterialModel(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    mechanism_models = models.ManyToManyField(MaterialMechanismModel, related_name='material_models')
    access = models.CharField(max_length=10, default='admin')

    def __str__(self):
        return self.material.name + " model"
