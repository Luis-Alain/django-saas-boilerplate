# Tests de Integración - Rutas Protegidas

## Descripción

Este módulo contiene los tests de integración para verificar que las **rutas protegidas** del proyecto funcionan correctamente. Las rutas protegidas son aquellas que requieren que el usuario esté autenticado para acceder.

## Concepto

| Tipo de usuario | Acceso a rutas protegidas |
|-----------------|---------------------------|
| **Anónimo** (no autenticado) | ❌ Redirigido a página de login |
| **Autenticado** | ✅ Acceso permitido |

## Decorador usado

Las rutas protegidas usan el decorador `@login_required` de Django. Cuando un usuario no autenticado intenta acceder, Django automáticamente lo redirige a la página de login configurada en `LOGIN_URL`.

## Rutas probadas

| Ruta | Vista | Requiere auth |
|------|-------|---------------|
| `/dashboard/` | Dashboard principal | ✅ |
| `/dashboard/profile/` | Perfil del usuario | ✅ |
| `/dashboard/settings/` | Configuración | ✅ |
| `/subscriptions/` | Gestión de suscripción | ✅ |

## Casos de prueba

### Usuario anónimo (no autenticado)

#### TC-PROTECT-001: Dashboard redirige a usuarios no autenticados

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que usuarios no autenticados son redirigidos al intentar acceder al dashboard |
| **Precondiciones** | Usuario no autenticado |
| **Resultado esperado** | - status_code = 302<br>- URL de redirección contiene `/accounts/login/` |

#### TC-PROTECT-002: Profile redirige a usuarios no autenticados

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que usuarios no autenticados son redirigidos al intentar acceder a profile |
| **Precondiciones** | Usuario no autenticado |
| **Resultado esperado** | status_code = 302 |

#### TC-PROTECT-003: Settings redirige a usuarios no autenticados

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que usuarios no autenticados son redirigidos al intentar acceder a settings |
| **Precondiciones** | Usuario no autenticado |
| **Resultado esperado** | status_code = 302 |

#### TC-PROTECT-004: Subscription redirige a usuarios no autenticados

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que usuarios no autenticados son redirigidos al intentar acceder a subscription |
| **Precondiciones** | Usuario no autenticado |
| **Resultado esperado** | status_code = 302 |

---

### Usuario autenticado

#### TC-PROTECT-005: Usuario autenticado puede acceder al dashboard

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que usuarios autenticados pueden acceder al dashboard |
| **Precondiciones** | Usuario autenticado (force_login) |
| **Resultado esperado** | status_code = 200 |

#### TC-PROTECT-006: Usuario autenticado puede acceder a profile

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que usuarios autenticados pueden acceder a profile |
| **Precondiciones** | Usuario autenticado (force_login) |
| **Resultado esperado** | status_code = 200 |

#### TC-PROTECT-007: Usuario autenticado puede acceder a settings

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que usuarios autenticados pueden acceder a settings |
| **Precondiciones** | Usuario autenticado (force_login) |
| **Resultado esperado** | status_code = 200 |

#### TC-PROTECT-008: Usuario autenticado puede acceder a subscription

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Verifica que usuarios autenticados pueden acceder a subscription |
| **Precondiciones** | Usuario autenticado (force_login) |
| **Resultado esperado** | status_code = 200 |

## Ejecutar tests

```bash
python manage.py test apps.accounts.tests.integration
```

## Archivo

- `test_protected_routes.py` - 8 tests

## Funciones de ayuda usadas

- `self.client.force_login(user)`: Simula login sin necesidad de password (útil para tests)
- `response.status_code`: Verifica código HTTP de respuesta
- `response.url`: Verifica URL de redirección