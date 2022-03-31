from django.contrib import admin
from strains.models import Batch, Rating, Strain, TerpeneProfile, Grower

# Register your models here.


class BatchAdmin(admin.ModelAdmin):
    pass


class RatingAdmin(admin.ModelAdmin):
    pass


class StrainAdmin(admin.ModelAdmin):
    pass


class TerpeneProfileAdmin(admin.ModelAdmin):
    pass


class GrowerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Batch, BatchAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Strain, StrainAdmin)
admin.site.register(TerpeneProfile, TerpeneProfileAdmin)
admin.site.register(Grower, GrowerAdmin)
