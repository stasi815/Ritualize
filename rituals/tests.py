from django.test import TestCase
from django.contrib.auth.models import User
from rituals.models import Ceremony
from rituals.views import CeremonyForm
from django.urls import reverse_lazy
# Create your tests here.

class CeremonyTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def test_ceremony_slugify_on_save(self):
        """ Tests the slug generated when saving a Ceremony object. """
        user = User()
        user.save()

        ceremony = Ceremony(title="concentration", content="test", author=user)
        ceremony.save()

        self.assertEqual(ceremony.slug, "my-test-ceremony")
