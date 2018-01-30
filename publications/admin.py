from django.contrib import admin
from .models import *


class PublicationImageInline(admin.TabularInline):
    model = PublicationImage
    extra = 0


class PublicationTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PublicationType._meta.fields]

    class Meta:
        model = PublicationType


admin.site.register(PublicationType, PublicationTypeAdmin)


class PublicationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Publication._meta.fields]
    inlines = [PublicationImageInline]

    class Meta:
        model = Publication


admin.site.register(Publication, PublicationAdmin)


class PublicationImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PublicationImage._meta.fields]

    class Meta:
        model = PublicationImage


admin.site.register(PublicationImage, PublicationImageAdmin)


# Register your models here.
