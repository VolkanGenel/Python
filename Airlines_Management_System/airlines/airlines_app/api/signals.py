from django.db.models.signals import post_save
from django.dispatch import receiver
from airlines_app.models import Reservation
from airlines_app.utils.email_utils import send_email

@receiver(post_save, sender=Reservation, )
def send_email_signal(sender, instance, created, **kwargs):
    if created:
        to_email = instance.passenger_email
        if to_email:
            send_email(to_email, instance)