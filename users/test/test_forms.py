from django.test import TestCase
from django.contrib.auth.models import User
from users.forms import RegisterForm, LoginForm, UserUpdateForm, UpdateProfileForm
from users.models import Profile  # Don't forget to import the Profile model

class TestUserForms(TestCase):

    def test_register_form_valid(self):
        # Prepare valid form data
        form_data = {
            'first_name': 'pravin',
            'last_name': 'kannappan',
            'username': 'irpravin',
            'email': 'irpravin@gmail.com',
            'password1': 'pg030399',
            'password2': 'pg030399',
        }

        # Create form instance with valid data
        form = RegisterForm(data=form_data)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_user_update_form_valid(self):
        # Create a User instance
        user = User.objects.create_user(
            username='irpravin',
            email='irpravin@gmail.com',
            password='pg030399'
        )

        # Prepare valid form data for user update
        form_data = {
            'first_name': 'Pravin Updated',
            'last_name': 'kannappan Updated',
            'email': 'irpravin_updated@gmail.com',
        }

        # Create form instance with valid data
        form = UserUpdateForm(data=form_data, instance=user)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_update_profile_form_valid(self):
        # Create a User instance
        user = User.objects.create_user(
            username='irpravin',
            email='irpravin_updated@gmail.com',
            password='pg030399'
        )

        # Create a Profile instance for the user
        profile = Profile.objects.create(user=user)

        # Prepare valid form data for profile update
        form_data = {
            'avatar': 'user/desktop/pravin.jpg',
            'address': 'Tamilnadu, Chennai',
        }

        # Create form instance with valid data
        form = UpdateProfileForm(data=form_data, instance=profile)

        # Check if the form is valid
        self.assertTrue(form.is_valid())
