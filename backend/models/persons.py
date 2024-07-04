from django.db.models import (CharField, DateField, EmailField)
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel


class Person(TimeStampedModel):
    class Meta:
        verbose_name = _('Persona')
        verbose_name_plural = _("Personas")

    first_name = CharField(max_length=150, verbose_name=_('Nombre completo'))
    last_name = CharField(max_length=150, verbose_name=_('Apellidos'))
    date_of_birth = DateField(verbose_name=_('Data de nascimento'))
    email = EmailField(verbose_name=_('Correo electronico'))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
