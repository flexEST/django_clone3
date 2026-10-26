# django_clone_steam

A small Django project that serves a static copy of the Steam store homepage.

> **Note:** This repository does **not** modify the Django framework itself. It is a regular project created with `django-admin startproject` and `startapp`, plus the few changes listed below.

---

## Project layout

```
mydjango/
├── manage.py
├── mysite/                  # project package (django-admin startproject mysite)
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── steam/                   # app (manage.py startapp steam)
    ├── templates/
    │   └── index.html       # saved Steam store homepage
    ├── migrations/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
```

Generated with **Django 6.1.1**.

---

## What changed compared to a fresh Django project

A fresh `startproject` + `startapp` gives you the files above with default contents. These are the only differences.

### 1. `mysite/settings.py`
- Added the `steam` app to `INSTALLED_APPS`:
  ```python
  INSTALLED_APPS = [
      "django.contrib.admin",
      "django.contrib.auth",
      "django.contrib.contenttypes",
      "django.contrib.sessions",
      "django.contrib.messages",
      "django.contrib.staticfiles",
      "steam",          # <-- added
  ]
  ```
- Everything else is the default generated configuration (SQLite database, `DEBUG = True`, `ALLOWED_HOSTS = []`, UTC time zone, `en-us`, default middleware and password validators).

### 2. `mysite/urls.py`
- Added one route that maps `/steam/` to the `home` view:
  ```python
  from steam import views

  urlpatterns = [
      path("admin/", admin.site.urls),
      path("steam/", views.home, name="home"),   # <-- added
  ]
  ```

### 3. `steam/views.py`
- Added a single view that renders the template, with no context and no logic:
  ```python
  def home(request):
      return render(request, "index.html")
  ```

### 4. `steam/templates/index.html`
- Added a ~3,700-line static HTML page: a saved copy of the Steam store homepage ("Welcome to Steam").
- It is plain HTML. It uses **no** Django template tags or variables (`{% %}` / `{{ }}`).
- Its CSS, JavaScript and fonts are loaded from Steam's CDN (`store.fastly.steamstatic.com`), so the page needs an internet connection to look right.

### 5. `steam/apps.py`
- The config class is named `LibraryConfig` (a leftover name) but sets `name = 'steam'`, so it works as the `steam` app's config.

### Left at the Django default (empty)
- `steam/models.py`: no models
- `steam/admin.py`: nothing registered
- `steam/tests.py`: no tests
- `steam/migrations/`: only `__init__.py`
- `mysite/asgi.py`, `mysite/wsgi.py`, `manage.py`: unchanged

---

## What this project does not have (yet)

- No database models, so no games, users, cart or library
- No login or authentication beyond Django's built-in admin
- No static files folder; all assets come from Steam's CDN
- No dynamic data; the page is the same for every visitor
- No `requirements.txt`

---

## Running it

```bash
pip install django
cd mydjango
python manage.py migrate
python manage.py runserver
```

Then open <http://127.0.0.1:8000/steam/>.

---

## Before deploying

The default development settings are still in place and are not safe for production:

- `SECRET_KEY` is the auto-generated `django-insecure-...` key
- `DEBUG = True`
- `ALLOWED_HOSTS = []`
