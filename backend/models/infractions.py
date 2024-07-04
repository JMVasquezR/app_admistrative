from django.db.models import (TextField, ForeignKey, PROTECT, CASCADE)
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel

from backend.models.officials import Official
from backend.models.vehicles import Vehicle


class Infraction(TimeStampedModel):
    class Meta:
        verbose_name = _('Infracción')
        verbose_name_plural = _("Infracciones")

    vehicle = ForeignKey(Vehicle, on_delete=PROTECT, verbose_name=_('Vehículo'))
    comment = TextField(verbose_name=_('Comentarios'))
    official = ForeignKey(Official, on_delete=CASCADE, verbose_name=_('Oficial'))

    def __str__(self):
        return f"Infracción de {self.vehicle.plate_number} por {self.official}"
