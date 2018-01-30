from django.db import models


class PublicationType(models.Model):
    name = models.CharField(max_length=48, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.id, self.name)

    class Meta:
        verbose_name = 'Тип публикации'
        verbose_name_plural = 'Типы публикаций'


class Publication(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    main_block = models.TextField(blank=True, null=True, default=None)
    publication_type = models.ForeignKey(PublicationType, blank=True, null=True, default=None)
    author = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s %s" % (self.publication_type.name, self.name, self.id)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


class PublicationImage(models.Model):
    publication = models.ForeignKey(Publication, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='publications_images/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Фотография %s %s" % (self.publication, self.id)

    class Meta:
        verbose_name = 'Фотография публикации'
        verbose_name_plural = 'Фотографии публикаций'

# Create your models here.
