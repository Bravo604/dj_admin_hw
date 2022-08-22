from django.contrib import admin
from .models import *


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_purchase'
    list_display = ('owners_name', 'block', 'date_purchase', 'status', 'area', 'get_total_price')
    search_fields = ('owners_name',)
    fields = ('owners_name', 'block', 'date_purchase', 'status', 'area',)
    empty_value_display = '--без хоз--'
    list_editable = ('date_purchase',)

    @admin.display(description='Total price')
    def get_total_price(self, obj):
        return obj.area * obj.block.price


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('block_number', 'entrance_quantity', 'number_of_floors', 'get_apartments_on_floor')

    @admin.display(description='Apartments on floor')
    def get_apartments_on_floor(self, obj):
        return obj.number_of_apartments / obj.entrance_quantity / obj.number_of_floors

    # @admin.display(description='Total apartment price in block')
    # def get_total_ap_price(self, obj):
    #     return obj.number_of_apartments * obj.price * obj.apartment
    # не понял условия ведь у всех квартир может быть разня
    #площадь как вычислить стоимомть в блоке не допер)))
