"""
Test Case: Protected Routes Integration Tests

Tests de integración para rutas protegidas:
- Rutas que requieren autenticación redirigen usuarios anónimos
- Usuarios autenticados pueden acceder a rutas protegidas

Auteur: Luis-Alain
Date: 2026-04-05
"""

from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class ProtectedRoutesTests(TestCase):
    """
    Tests para rutas protegidas que requieren autenticación.

    Estas rutas deben:
    - Redirigir a usuarios no autenticados a la página de login
    - Permitir acceso a usuarios autenticados
    """

    def test_dashboard_redirects_anonymous_users(self):
        """
        TC-PROTECT-001: Dashboard redirige a usuarios no autenticados.
        """
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_profile_redirects_anonymous_users(self):
        """
        TC-PROTECT-002: Profile redirige a usuarios no autenticados.
        """
        response = self.client.get('/dashboard/profile/')
        self.assertEqual(response.status_code, 302)

    def test_settings_redirects_anonymous_users(self):
        """
        TC-PROTECT-003: Settings redirige a usuarios no autenticados.
        """
        response = self.client.get('/dashboard/settings/')
        self.assertEqual(response.status_code, 302)

    def test_subscription_page_redirects_anonymous_users(self):
        """
        TC-PROTECT-004: Subscription redirige a usuarios no autenticados.
        """
        response = self.client.get('/subscriptions/')
        self.assertEqual(response.status_code, 302)

    def test_authenticated_user_can_access_dashboard(self):
        """
        TC-PROTECT-005: Usuario autenticado puede acceder al dashboard.
        """
        user = User.objects.create_user(email='test@example.com', password='SecureP@ss123', is_active=True)
        self.client.force_login(user)

        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)

    def test_authenticated_user_can_access_profile(self):
        """
        TC-PROTECT-006: Usuario autenticado puede acceder a profile.
        """
        user = User.objects.create_user(email='test@example.com', password='SecureP@ss123', is_active=True)
        self.client.force_login(user)

        response = self.client.get('/dashboard/profile/')
        self.assertEqual(response.status_code, 200)

    def test_authenticated_user_can_access_settings(self):
        """
        TC-PROTECT-007: Usuario autenticado puede acceder a settings.
        """
        user = User.objects.create_user(email='test@example.com', password='SecureP@ss123', is_active=True)
        self.client.force_login(user)

        response = self.client.get('/dashboard/settings/')
        self.assertEqual(response.status_code, 200)

    def test_authenticated_user_can_access_subscription(self):
        """
        TC-PROTECT-008: Usuario autenticado puede acceder a subscription.
        """
        user = User.objects.create_user(email='test@example.com', password='SecureP@ss123', is_active=True)
        self.client.force_login(user)

        response = self.client.get('/subscriptions/')
        self.assertEqual(response.status_code, 200)
