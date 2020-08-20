from django.db import models
from django.utils.text import slugify
import itertools
import os


# Create your models here.
class Competition(models.Model):
    img = models.ImageField(upload_to="images/competitions")
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True,
                            default='',
                            editable=False,
                            blank=False)
    date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=False)
    about = models.TextField()

    def _generate_slug(self):
        max_length = self._meta.get_field('slug').max_length
        value = self.name
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Competition.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date', '-timestamp']

    def get_absolute_url(self):
        return f"/competitions/{self.slug}"

    def get_edit_url(self):
        return f"/competitions/{self.slug}/edit"

    def get_delete_url(self):
        return f"/competitions/{self.slug}/delete"

    def __str__(self):
        return self.name
