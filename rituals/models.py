from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Ceremony(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.PROTECT, help_text="The user that posted this ceremony.")
    slug = models.CharField(max_length=settings.CEREMONY_PAGE_TITLE_MAX_LENGTH, blank=True, editable=False, help_text="Unique URL path to access this page. Generated by the system.")
    content = models.TextField(help_text="Write the description of the ceremony here.")
    created = models.DateTimeField(auto_now_add=True, help_text="The date and time this page was created. Automatically generated when the model saves.")
    modified = models.DateTimeField(auto_now=True, help_text="The date and time this page was updated. Automatically generated when the model updates.")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/my-new-ceremony-page). """
        path_components = {'slug': self.slug}
        return reverse("ceremony-details-page", kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new page is created. """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        return super(Ceremony, self).save(*args, **kwargs)