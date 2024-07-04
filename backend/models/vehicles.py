from django.db.models import (CharField, ForeignKey, PROTECT)
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel

from backend.models.persons import Person


class Vehicle(TimeStampedModel):
    class Meta:
        verbose_name = _('Vehiculo')
        verbose_name_plural = _("Vehiculos")

    plate_number = CharField(max_length=6, verbose_name=_('Número de placa'))
    brand = CharField(max_length=50, verbose_name=_('Marca'))
    color = CharField(max_length=50, verbose_name=_('Color'))
    person = ForeignKey(Person, on_delete=PROTECT)

    def __str__(self):
        return f"{self.plate_number}"
