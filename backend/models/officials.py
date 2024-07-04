from django.contrib.auth.models import User
from django.db.models import (CharField, OneToOneField, CASCADE)
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel


class Official(TimeStampedModel):
    class Meta:
        verbose_name = _('Oficial')
        verbose_name_plural = _("Oficiales")

    first_name = CharField(max_length=150, verbose_name=_('Nombre completo'))
    last_name = CharField(max_length=150, verbose_name=_('Apellidos'))
    code = CharField(max_length=100, unique=True, blank=True, verbose_name=_('Codigo'))
    user = OneToOneField(User, on_delete=CASCADE, null=True, blank=True, verbose_name=_('Usuario'))

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_unique_codigo()
        super(Official, self).save(*args, **kwargs)

    def generate_unique_codigo(self):
        year = now().year
        base_code = f"{year}_{self.first_name[:2].upper()}{self.last_name[:2].upper()}"
        unique_code = base_code
        num = 1

        while Official.objects.filter(code=unique_code).exists():
            unique_code = f"{base_code}{num}"
            num += 1

        return unique_code

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


@receiver(post_save, sender=Official)
def crear_usuario_oficial(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create_user(username=instance.code)
        instance.user = user
        instance.save()
