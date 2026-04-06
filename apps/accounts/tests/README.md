# Tests de Autenticación

Este módulo contiene los casos de prueba para el sistema de autenticación del proyecto.

## Estructura

```
tests/
├── models/              # Tests del modelo CustomUser
│   └── test_custom_user.py
├── views/               # Tests de las vistas de auth
│   ├── test_auth_views.py
│   └── test_email_verification.py
└── integration/        # Tests de rutas protegidas
    └── test_protected_routes.py
```

## Cómo ejecutar los tests

```bash
# Todos los tests del proyecto
make test

# Solo tests de accounts
python manage.py test apps.accounts.tests

# Por categoría
python manage.py test apps.accounts.tests.models         # 7 tests
python manage.py test apps.accounts.tests.views          # 20 tests (auth + email)
python manage.py test apps.accounts.tests.views.test_auth_views  # 12 tests
python manage.py test apps.accounts.tests.views.test_email_verification  # 8 tests
python manage.py test apps.accounts.tests.integration    # 8 tests

# Tests de otras apps
python manage.py test apps.dashboard.tests
python manage.py test apps.landing.tests
```

## Resumen de cobertura

### accounts (35 tests)

| Categoría | Tests | Descripción |
|-----------|-------|-------------|
| **Models** | 7 | Modelo CustomUser: crear usuario, superuser, validaciones |
| **Views - Auth** | 12 | Vistas: signup, login, logout |
| **Views - Email** | 8 | Flujo de verificación de email |
| **Integration** | 8 | Rutas protegidas: dashboard, profile, settings, subscription |

### Resumen completo del proyecto

| App | Tests |
|-----|-------|
| accounts | 35 |
| dashboard | ? |
| landing | ? |
| **Total** | **45** |

## Convenciones de nomenclatura

- **TC-AUTH-XXX**: Test Case de autenticación (modelo)
- **TC-SIGNUP-XXX**: Test Case de registro
- **TC-LOGIN-XXX**: Test Case de login
- **TC-LOGOUT-XXX**: Test Case de logout
- **TC-PROTECT-XXX**: Test Case de rutas protegidas
- **TC-VERIFY-XXX**: Test Case de verificación de email

## Casos de prueba (accounts)

### Models (CustomUser)

| Código | Descripción |
|--------|-------------|
| TC-AUTH-001 | Crear usuario con email y password válidos |
| TC-AUTH-002 | Crear usuario sin email lanza error |
| TC-AUTH-003 | Crear usuario con email inválido (permite) |
| TC-AUTH-004 | Crear superuser con credenciales válidas |
| TC-AUTH-005 | Crear superuser sin password |
| TC-AUTH-006 | __str__ retorna email |
| TC-AUTH-007 | username es None |

### Views (Auth)

| Código | Descripción |
|--------|-------------|
| TC-SIGNUP-001 | Página de signup retorna 200 |
| TC-SIGNUP-002 | Página contiene formulario |
| TC-SIGNUP-003 | Signup con datos válidos crea usuario |
| TC-SIGNUP-004 | Email único - no permite duplicados |
| TC-SIGNUP-005 | Modelo permite cualquier email |
| TC-LOGIN-001 | Página de login retorna 200 |
| TC-LOGIN-002 | Página contiene formulario |
| TC-LOGIN-003 | Login con credenciales válidas autentica |
| TC-LOGIN-004 | Login con password incorrecto falla |
| TC-LOGIN-005 | Login con email inexistente falla |
| TC-LOGOUT-001 | Logout requiere autenticación |
| TC-LOGOUT-002 | Logout cierra sesión |

### Views (Email Verification)

| Código | Descripción |
|--------|-------------|
| TC-VERIFY-001 | Signup crea EmailAddress no verificado |
| TC-VERIFY-002 | Signup redirige a página de verificación |
| TC-VERIFY-003 | Página de confirmación carga correctamente |
| TC-VERIFY-004 | Clave de confirmación funciona |
| TC-VERIFY-005 | Email verificado permite login |
| TC-VERIFY-006 | Email no verificado |
| TC-VERIFY-007 | Página de reenvío requiere auth |
| TC-VERIFY-008 | Creación de EmailConfirmation |

### Integration (Protected Routes)

| Código | Descripción |
|--------|-------------|
| TC-PROTECT-001 | Dashboard redirige anónimos |
| TC-PROTECT-002 | Profile redirige anónimos |
| TC-PROTECT-003 | Settings redirige anónimos |
| TC-PROTECT-004 | Subscription redirige anónimos |
| TC-PROTECT-005 | Usuario autenticado puede acceder a dashboard |
| TC-PROTECT-006 | Usuario autenticado puede acceder a profile |
| TC-PROTECT-007 | Usuario autenticado puede acceder a settings |
| TC-PROTECT-008 | Usuario autenticado puede acceder a subscription |

## Requisitos

- Django 6.0
- Python 3.12
- django-allauth instalado y configurado