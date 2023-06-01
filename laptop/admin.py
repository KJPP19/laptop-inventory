from django.contrib import admin
from .models import UserInfo, Laptop, DamagedUnit


class UserInfoItemAmin(admin.ModelAdmin):
    list_display = ['name', 'added_at', 'updated_at']


class LaptopItemAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 
                    'status', 'current_user', 
                    'added_at', 'updated_at']


class DamagedUnitItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'laptop', 
                    'damage_type', 'added_at', 
                    'updated_at']


admin.site.register(UserInfo, UserInfoItemAmin)
admin.site.register(Laptop, LaptopItemAdmin)
admin.site.register(DamagedUnit, DamagedUnitItemAdmin)


