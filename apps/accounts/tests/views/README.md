# Tests de Vistas de Autenticación

## Descripción

Este módulo contiene los tests para las vistas de autenticación del proyecto: **Signup** (registro), **Login** (inicio de sesión) y **Logout** (cierre de sesión).

Estas vistas están configuradas en **django-allauth**, no en código propio del proyecto.

## URLs de las vistas

| Vista | URL | Método |
|-------|-----|--------|
| Signup | `/accounts/signup/` | GET, POST |
| Login | `/accounts/login/` | GET, POST |
| Logout | `/accounts/logout/` | GET, POST |

## Casos de prueba

### Signup (Registro)

#### TC-SIGNUP-001: La página de signup retorna código 200

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que la página de registro está disponible |
| **Precondiciones** | Ninguna |
| **Resultado esperado** | `response.status_code == 200` |

#### TC-SIGNUP-002: La página de signup contiene el formulario

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que el formulario de registro está presente |
| **Precondiciones** | Ninguna |
| **Resultado esperado** | Contains: csrfmiddlewaretoken, email, password1, password2 |

#### TC-SIGNUP-003: El modelo permite crear usuarios con datos válidos

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que el modelo CustomUser permite crear usuarios correctamente |
| **Precondiciones** | Ninguna |
| **Resultado esperado** | Usuario creado con email y password correctos |
| **Nota** | El test completo de POST requiere la UI de allauth. Aquí probamos el modelo directamente. |

#### TC-SIGNUP-004: Email único - no se permiten duplicados

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que no se pueden crear dos usuarios con el mismo email |
| **Precondiciones** | Usuario existente con email |
| **Resultado esperado** | Lanza `IntegrityError` al intentar crear otro usuario con el mismo email |

#### TC-SIGNUP-005: El modelo permite crear usuarios con cualquier email

| Campo | Descripción |
|-------|-------------|
| **Descripción** | El modelo no valida formato de email (solo que no esté vacío) |
| **Precondiciones** | Ninguna |
| **Resultado esperado** | Usuario creado con cualquier string como email |
| **Nota** | La validación de formato ocurre en los forms, no en el modelo |

---

### Login (Inicio de sesión)

#### TC-LOGIN-001: La página de login retorna código 200

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que la página de login está disponible |
| **Precondiciones** | Ninguna |
| **Resultado esperado** | `response.status_code == 200` |

#### TC-LOGIN-002: La página de login contiene el formulario

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que el formulario de login está presente |
| **Precondiciones** | Ninguna |
| **Resultado esperado** | Contains: csrfmiddlewaretoken, login, password |

#### TC-LOGIN-003: Login con credenciales válidas autentica al usuario

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que `authenticate()` retorna el usuario para credenciales válidas |
| **Precondiciones** | Usuario creado con is_active=True |
| **Resultado esperado** | `authenticate()` retorna el usuario |
| **Nota** | El test completo de POST requiere la UI de allauth. |

#### TC-LOGIN-004: El modelo rechaza password incorrecto

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que `authenticate()` retorna None para password incorrecto |
| **Precondiciones** | Usuario creado |
| **Resultado esperado** | `authenticate()` retorna None |

#### TC-LOGIN-005: authenticate() retorna None para email inexistente

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que no se puede autenticar con un email que no existe |
| **Precondiciones** | Ninguna |
| **Resultado esperado** | `authenticate()` retorna None |

---

### Logout (Cierre de sesión)

#### TC-LOGOUT-001: Logout requiere que el usuario esté autenticado

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que usuarios no autenticados son redirigidos |
| **Precondiciones** | Usuario no autenticado |
| **Resultado esperado** | `response.status_code == 302` (redirige a login) |

#### TC-LOGOUT-002: Logout cierra la sesión del usuario

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que después de logout, el usuario no puede acceder a rutas protegidas |
| **Precondiciones** | Usuario autenticado |
| **Resultado esperado** | Después de POST a logout: dashboard retorna 302 |
| **Nota** | allauth requiere POST para logout (con csrf token) |

## Limitaciones

**Importante**: Los tests de vistas POST completos no están disponibles porque requieren la UI de allauth configurada en el entorno de test.

Los tests usan:
- **GET**: Para verificar que las páginas cargan correctamente
- **authenticate()**: Para verificar la autenticación funciona a nivel de modelo

## Ejecutar tests

```bash
python manage.py test apps.accounts.tests.views
```

## Archivo

- `test_auth_views.py` - 12 tests