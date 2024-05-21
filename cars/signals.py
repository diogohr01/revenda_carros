from django.db.models.signals import pre_save, pre_delete, post_delete, post_save
from django.dispatch import receiver
from cars.models import Car

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    print(' ### PRE SAVE ###')
    print(instance)
    
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    print(' ### POST SAVE ###')
    print(instance)
    
@receiver(pre_delete, sender=Car)
def car_post_save(sender, instance, **kwargs):
    print(' ### PRE DELETE ###')
    print(instance)
    
@receiver(post_delete, sender=Car)
def car_post_save(sender, instance, **kwargs):
    print(' ### POST DELETE ###')
    print(instance)