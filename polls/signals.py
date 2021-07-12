from django.db.models.signals import pre_save
from django.dispatch import receiver, Signal

from polls.models import Question


ping = Signal()


@receiver(pre_save, sender=Question)
def question_pre_save(sender, **kwargs):
    print(sender)
    print(kwargs)
    ping.send(None)
    print("Sent")


@receiver(ping)
def pong(sender, **kwargs):
    print("Pong!")
    print(sender)