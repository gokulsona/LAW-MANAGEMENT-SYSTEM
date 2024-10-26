from django.contrib import admin
from . models import LawList, Lawyers, DetailLaw, CourtDistrict, Court, Cases

# Register your models here.

admin.site.register(LawList)
admin.site.register(Lawyers)
admin.site.register(DetailLaw)
admin.site.register(CourtDistrict)
admin.site.register(Court)
admin.site.register(Cases)