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

        c = Ceremony(title="Test Concentration", content="test", author=user)
        c.save()

        self.assertEqual(c.slug, "test-concentration")

class CeremonyListViewTests(TestCase):
    def test_multiple_pages(self):
        """ Tests that we see multiple pages on landing page. """
        user = User.objects.create()

        Ceremony.objects.create(title="test ceremony", content="test", author=user)
        Ceremony.objects.create(title="another test ceremony", content="test", author=user)

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

        responses = response.context['ceremonies']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<Ceremony: test ceremony>', '<Ceremony: another test ceremony>'],
            ordered=False
        )
