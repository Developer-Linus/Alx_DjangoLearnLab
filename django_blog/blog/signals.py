# Signals trigger a specific action in the modification/change of an entry in a database.
# We have a sender and a receiver
# Sender is the model that notifies a receiver when an event occurs.
#Receiver acts based on the notification it receives.
# The connection between sender and receiver is achieved through signal dispatcher.
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver #interface sitting between sender and the receiver.

from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
        