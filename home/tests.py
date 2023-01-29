from django.test import SimpleTestCase
from django.urls import reverse, resolve
from . import views


class TestUrls(SimpleTestCase):
    ''' Tests for testing URL resolutions for each view. '''

    def test_home_url_is_resolved(self):
        ''' Tests home URL resolution '''
        url = reverse('home:home')
        self.assertEqual(resolve(url).func, views.home)

    def test_reviews_url_is_resolved(self):
        ''' Tests reviews URL resolution '''
        url = reverse('home:reviews')
        self.assertEqual(resolve(url).func, views.reviews)

    def test_residents_url_is_resolved(self):
        ''' Tests health hub tracker URL resolution '''
        url = reverse('home:residents')
        self.assertEqual(resolve(url).func, views.residents)

    def test_contact_us_url_is_resolved(self):
        ''' Tests contact us URL resolution '''
        url = reverse('home:contact_us')
        self.assertEqual(resolve(url).func.view_class, views.ContactUs)

    def test_delete_review_url_is_resolved(self):
        ''' Tests delete review URL resolution '''
        id_x = int()
        url = reverse('home:delete_review', args=[id_x])
        self.assertEqual(resolve(url).func.view_class, views.DeleteReview)

    def test_edit_review_url_is_resolved(self):
        ''' Tests edit review URL resolution '''
        id_x = int()
        url = reverse('home:edit_review', args=[id_x])
        self.assertEqual(resolve(url).func.view_class, views.EditReview)

    def test_add_review_url_is_resolved(self):
        ''' Tests add review URL resolution '''
        url = reverse('home:add_review')
        self.assertEqual(resolve(url).func.view_class, views.AddReview)