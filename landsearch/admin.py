from django.contrib import admin
from .models import RationCard, FamMember, RevenueDetail, LookUp

# admin.site.register(RationCard)
# admin.site.register(FamMember)

@admin.register(FamMember)
class FamMemberAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'card', 'age', 'maritial_status', 'relation', 'job', 'income')
    fields = [('name', 'card'), ('age', 'maritial_status', 'relation'), ('job', 'income')]

@admin.register(RationCard)
class RationCardAdmin(admin.ModelAdmin):
    list_display = ( 'card_no', 'Card_Type', 'house_name', 'place', 'district')
    fieldsets = (
        ('Card Details', {
            'fields': ('card_no', 'Card_Type')
        }),
        ('Address', {
            'fields': ('house_name', 'place', 'pin_no', 'taluk', 'district')
        }),
    )
@admin.register(RevenueDetail)
class RevenueDetailAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'land', 'district', 'land_type')
    fields = [('name', 'land'), ('district', 'land_type')]

    
@admin.register(LookUp)
class LookUpAdmin(admin.ModelAdmin):
    list_display = ( 'district', 'a', 'b', 'c', 'd', 'e', 'f')
    fields = ['district', ('a', 'b', 'c', 'd', 'e', 'f')]



# # Define the admin class
# class RationCardAdmin(admin.ModelAdmin):
#     pass

# # Register the admin class with the associated model
# admin.site.register(RationCard, RationCardAdmin)