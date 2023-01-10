from django.contrib import admin
from .models import Order, OrderDetail


class OrderDetailAdmin(admin.TabularInline):
    model = OrderDetail
    readonly_fields = ('subtotal',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderDetailAdmin,)

    readonly_fields = ('order_number', 'date',
                       'order_total',)

    fields = ('order_number', 'user', 'first_name', 'last_name',
              'email', 'phone_number', 'date', 'street_address_1',
              'street_address_2', 'city', 'postcode', 'county', 'country',
              'order_total',)

    list_display = ('user', 'order_number', 'date', 'first_name', 'last_name',
                    'order_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
