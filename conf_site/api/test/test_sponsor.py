from django.core.urlresolvers import reverse

from rest_framework import status
from symposion.sponsorship.models import Sponsor

from .base import TestBase


class TestSponsor(TestBase):

    @classmethod
    def setUpTestData(cls):
        super(TestSponsor, cls).setUpTestData()
        cls.sponsor = Sponsor.objects.first()

    def test_speaker_list_api_anonymous_user(self):
        response = self.client.get(reverse('sponsor-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(
            {
                'name': self.sponsor.name,
                'external_url': self.sponsor.external_url,
                'contact_name': self.sponsor.contact_name,
                'contact_email': self.sponsor.contact_email,
                'level': str(self.sponsor.level),
                'absolute_url': self.sponsor.get_absolute_url(),
                'annotation': self.sponsor.annotation,
            },
            response.data
        )

    def test_speaker_detail_api_anonymous_user(self):
        response = self.client.get(
            reverse('sponsor-detail',args=[self.sponsor.pk])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            {
                'name': self.sponsor.name,
                'external_url': self.sponsor.external_url,
                'contact_name': self.sponsor.contact_name,
                'contact_email': self.sponsor.contact_email,
                'level': str(self.sponsor.level),
                'absolute_url': self.sponsor.get_absolute_url(),
                'annotation': self.sponsor.annotation,
            },
            response.data
        )
