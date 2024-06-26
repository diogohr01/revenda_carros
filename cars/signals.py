from django.db.models.signals import pre_save, pre_delete, post_delete, post_save
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory


def car_inventory_update():
    cars_count = Car.objects.all().count() or 0
    cars_value = Car.objects.aggregate(total_value = Sum('value'))['total_value'] or 0
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
        )

@receiver(pre_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()
    
@receiver(pre_delete, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()
        
        
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

    
@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()

    
