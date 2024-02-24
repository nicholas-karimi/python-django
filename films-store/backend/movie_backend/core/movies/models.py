from django.db import models
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager


class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    director = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movies/')
    release_date = models.DateField()
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    tags = TaggableManager()
    # seasons
    # rating
    # actors
    # genres

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        # ordering = ['-release_date']
        ordering = ['-created_at']
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    

