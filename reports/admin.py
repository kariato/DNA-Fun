from django.contrib import admin

# Register your models here.

from .models import DNAKits,DNAMatches,DNASegment

admin.site.register(DNAKits)
admin.site.register(DNAMatches)
admin.site.register(DNASegment)