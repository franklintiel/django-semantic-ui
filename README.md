# Django Semantic UI
Easy python package that allow install, configure and use Semantic UI Framework with a Django project.

### Requirements
- npm (last stable version)
- Python 2.7.x
- Django 1.11.x

## Installing
- Install gulp (CLI), the version 3.9.1 is the available to work with Semantic UI Framework.
```shell
$ sudo npm install -g gulp@3.9.1
```

- Install the django-semantic-ui package:
```shell
$ pip install django-semantic-ui
```

- Configure django-semantic-ui in the settings.py:
```python
INSTALLED_APPS = [
    ...,
    'django_semantic_ui',
]
```

- Running the install command
```shell
$ python manage.py semantic_ui install
```
**NOTE:** You need to define the settings required to install semantic-ui module, see: [Install Semantic](https://semantic-ui.com/introduction/getting-started.html)
- You can use the follow options when the semantic-ui module is configured:
```shell
❯ Automatic (Use default locations and all components)

? We detected you are using NPM Nice! Is this your project folder? /home/franklinitiel/Documents/TSJ/projects/personal/python_tests/semanticui/static (Use arrow keys)
❯ Yes

? Where should we put Semantic UI inside your project? (semantic/) semantic
```

- Running the gulp build command
```shell
$ python manage.py semantic_ui gulp_build --semantic_folder=semantic
```
**NOTE**: The argument "--semantic_folder" is the name assigned to the "semantic" folder on the above step

## Settings

- Configure the static files and folder, see: [Managing static files](https://docs.djangoproject.com/en/1.11/howto/static-files/)
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    ...,
    ('semantic', os.path.join(BASE_DIR, 'static/semantic')),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

- Add 'django.template.context_processors.static' to context_processors option on the TEMPLATES settings
```python
# settings.py
# TEMPLATES settings
'context_processors': [
    ...,
    'django.template.context_processors.static',
    ...,
]
```

- Add CSS and JS to your django project
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Semantic UI Test</title>
    <link type="text/css" rel="stylesheet" href="{{ STATIC_URL }}semantic/dist/semantic.min.css">
</head>
<body>
    <h1>Title example</h1>
    <button>Button Test example</button>
    <script src="https://code.jquery.com/jquery-3.1.1.min.js" integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=" crossorigin="anonymous"></script>
    <script src="{{ STATIC_URL }}semantic/dist/semantic.min.js"></script>
</body>
</html>
```

## Additional settings
- GULP_VERSION by default is None, if you want to install a specific version of gulp module (local), you can use this settings, by example:
```python
# settings.py
GULP_VERSION = '3.9.1'
```

- SEMANTIC_UI_VERSION by default is None, if you want to install a specific version of semantic-ui module (local), you can use this settings, by example:
```python
# settings.py
SEMANTIC_UI_VERSION = '^2.4.2'
```

## Uninstall django-semantic-ui
- You can uninstall Semantic UI Framework and Gulp (local version) using the follow command:
```shell
$ python manage.py semantic_ui uninstall --semantic_folder=semantic
```

## Releases notes:

- 1.0.0: Initial and beta version (only installation and settings).
- 1.0.1: Bugs fixed semantic folder not found or not exists.
- 1.0.2: Bugs fixed semantid and static folders not found or not exists.
- 1.0.3: README.md file updated, bugs fixed self.semantic_ui_version undefined.
