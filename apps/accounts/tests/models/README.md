# Tests del Modelo CustomUser

## Descripción

El modelo `CustomUser` es un usuario personalizado que reemplaza el modelo de usuario de Django por defecto. Utiliza **email** como identificador único en lugar de username.

## Características del modelo

| Característica | Valor |
|---------------|-------|
| `USERNAME_FIELD` | `email` |
| `username` | `None` (no existe) |
| `email` | `EmailField` único |
| `REQUIRED_FIELDS` | `[]` (vacío) |

## Casos de prueba

### TC-AUTH-001: Crear usuario con email y password válidos

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que se puede crear un usuario con email y password válidos |
| **Precondiciones** | Ninguna |
| **Resultado esperado** | - Email almacenado correctamente<br>- Password hasheado correctamente<br>- is_staff = False<br>- is_superuser = False |

### TC-AUTH-002: Crear usuario sin email lanza error

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que el modelo no permite usuarios sin email |
| **Precondiciones** | Ninguna |
| **Resultado esperado** | Lanza `ValueError` con mensaje "Email is required" |

### TC-AUTH-003: Crear usuario con email inválido (formato)

| Campo | Descripción |
|-------|-------------|
| **Descripción** | El modelo permite crear usuarios con cualquier string como email |
| **Precondiciones** | Ninguna |
| **Resultado esperado** | El usuario se crea correctamente (la validación de formato ocurre en los forms, no en el modelo) |
| **Nota** | Este comportamiento es correcto por diseño. Los forms de Django/allauth validan el formato. |

### TC-AUTH-004: Crear superuser con credenciales válidas

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que se puede crear un superuser con is_staff y is_superuser |
| **Precondiciones** | Ninguna |
| **Resultado esperado** | - is_staff = True<br>- is_superuser = True<br>- Email almacenado correctamente |

### TC-AUTH-005: Crear superuser sin password

| Campo | Descripción |
|-------|-------------|
| **Descripción** | El modelo permite crear superusers sin password |
| **Precondiciones** | Ninguna |
| **Resultado esperado** | El superuser se crea correctamente |
| **Nota** | La validación de password ocurre en los forms, no en el modelo |

### TC-AUTH-006: La representación string del usuario es su email

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que `str(user)` retorna el email del usuario |
| **Precondiciones** | Usuario creado |
| **Resultado esperado** | `str(user) == 'test@example.com'` |

### TC-AUTH-007: username es None (email-only)

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que el campo username no existe (es None) |
| **Precondiciones** | Usuario creado |
| **Resultado esperado** | `user.username is None` |

## Ejecutar tests

```bash
python manage.py test apps.accounts.tests.models
```

## Archivo

- `test_custom_user.py` - 7 tests