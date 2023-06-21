from django.contrib import admin
from burgers.models import Burger, Drink


# Register your models here.
@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    pass


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    pass
