from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from users.views import RegisterView, CustomLoginView, update_user, ViewUserProfileView


class TestViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='mash', email='mash@gmail.com', password='Tinksg0303!kk')
        self.user.save()

    def test_register_view_get(self):
        # Test GET request to register view
        request = self.factory.get(reverse('users:users-register'))
        request.user = self.user  # Set the user attribute on the request
        response = RegisterView.as_view()(request)

        # Follow the redirect if the response status code is 302
        if response.status_code == 302:
            response = self.client.get(response.url)  # Use the client to follow the redirect

        self.assertEqual(response.status_code, 200)  # Check if the final response status code is 200 OK


    def test_custom_login_view_get(self):
        # Test GET request to custom login view
        request = self.factory.get(reverse('users:login'))
        request.user = self.user  # Set the user attribute on the request
        response = CustomLoginView.as_view()(request)
        self.assertEqual(response.status_code, 200)  # Check if the view returns 200 OK

    def test_update_user_view_get(self):
        # Test GET request to update_user view
        request = self.factory.get('/edit-management')
        request.user = self.user  # Set the user attribute on the request
        response = update_user(request)
        self.assertEqual(response.status_code, 200)  # Check if the view returns 200 OK

    def test_view_user_profile_view(self):
        # Test GET request to view_user_profile view
        request = self.factory.get('/profile-management')
        request.user = self.user  # Set the user attribute on the request
        response = ViewUserProfileView.as_view()(request)
        self.assertEqual(response.status_code, 200)  # Check if the view returns 200 OK
