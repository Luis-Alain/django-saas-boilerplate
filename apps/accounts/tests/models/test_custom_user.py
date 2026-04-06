"""
Test Case: CustomUser Model Tests

Tests para el modelo CustomUser:
- Crear usuario con email y password válidos
- Validación de email requerido
- Crear superuser
- Representación string del usuario
- Verificar que username es None (email-only)

Auteur: Luis-Alain
Date: 2026-04-05
"""

from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class CustomUserModelTests(TestCase):
    """
    Tests para el modelo CustomUser.

    El modelo CustomUser es un usuario personalizado que:
    - No tiene username (username=None)
    - Usa email como identificador único (USERNAME_FIELD='email')
    - Requiere email para ser creado
    """

    def test_create_user_with_valid_email_and_password(self):
        """
        TC-AUTH-001: Crear usuario con email y password válidos.

        Verifica que:
        - El email se almacena correctamente
        - La contraseña se hashea correctamente
        - El usuario no es staff ni superuser por defecto
        """
        user = User.objects.create_user(email='test@example.com', password='SecureP@ss123')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('SecureP@ss123'))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_without_email_raises_error(self):
        """
        TC-AUTH-002: Crear usuario sin email debe lanzar ValueError.

        Verifica que el modelo no permite usuarios sin email.
        """
        with self.assertRaises(ValueError) as context:
            User.objects.create_user(email='', password='testpass123')
        self.assertIn('Email is required', str(context.exception))

    def test_create_user_with_invalid_email_format_succeeds(self):
        """
        TC-AUTH-003: Crear usuario con email inválido (formato) es permitido por el modelo.

        Nota: El modelo CustomUser NO valida formato de email, solo que no esté vacío.
        La validación de formato ocurre en los forms, no en el modelo.
        """
        user = User.objects.create_user(email='not-an-email', password='testpass123')
        self.assertEqual(user.email, 'not-an-email')

    def test_create_superuser_with_valid_credentials(self):
        """
        TC-AUTH-004: Crear superuser con credenciales válidas.

        Un superuser debe tener:
        - is_staff = True
        - is_superuser = True
        """
        user = User.objects.create_superuser(email='admin@example.com', password='AdminP@ss123')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertEqual(user.email, 'admin@example.com')

    def test_create_superuser_without_password_succeeds(self):
        """
        TC-AUTH-005: Crear superuser sin password es posible (permite passwords vacíos).

        Nota: El modelo no valida que el password exista. La validación ocurre en forms.
        """
        user = User.objects.create_superuser(email='admin@example.com', password=None)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_user_str_returns_email(self):
        """
        TC-AUTH-006: La representación string del usuario debe ser su email.
        """
        user = User.objects.create_user(email='test@example.com', password='testpass123')
        self.assertEqual(str(user), 'test@example.com')

    def test_username_is_none(self):
        """
        TC-AUTH-007: Verificar que username es None (email-only).
        """
        user = User.objects.create_user(email='test@example.com', password='testpass123')
        self.assertIsNone(user.username)
