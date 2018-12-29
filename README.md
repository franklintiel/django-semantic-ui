# Django Semantic UI
Easy python package that allow install, configure and use Semantic UI Framework with a Django project.

### Requirements
- npm (last stable version)
- Python 2.7.x
- Django 1.11.x

## Installing
1) Install gulp (CLI), the version 3.9.1 is the available to work with Semantic UI Framework.
```shell
$ sudo npm install -g gulp@3.9.1
```

2) Install the django-semantic-ui package:
```shell
$ pip install django-semantic-ui
```

3) Configure django-semantic-ui in the settings.py:
```python
INSTALLED_APPS = [
    ...,
    'django_semantic_ui',
]
```

4) Running the install command
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

5) Running the gulp build command
```shell
$ python manage.py semantic_ui gulp_build
```
## Settings Development or Local environment

6) Add 'django.template.context_processors.static' to context_processors option on the TEMPLATES settings
```python
# settings.py
# TEMPLATES settings
'context_processors': [
    ...,
    'django.template.context_processors.static',
    ...,
]
```

7) Configure the static files and folder, see: [Managing static files](https://docs.djangoproject.com/en/1.11/howto/static-files/)
```python
STATIC_URL = '/static/'
```

8) Add CSS and JS to your django project
```html
{% load dsu %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Semantic UI Test</title>
    {% dsu_stylesheet_url %}
</head>
<body>
    <!-- Your HTML code -->
    {% dsu_jquery_url %}
    {% dsu_javascript_url %}
</body>
</html>
```

## Settings Production environment
- Configure the static files and folder, see: [Managing static files](https://docs.djangoproject.com/en/1.11/howto/static-files/)
```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
- And execute the collectstatic command
```shell
$ python manage.py collectstatic
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
- SEMANTIC_DIRNAME by default is 'semantic'', if you defined a custom dirname for the JS and CSS files when the Semantic UI Framework was installed (step 4), you need to add it on this settings.
```python
# settings.py
SEMANTIC_DIRNAME = 'semantic'
```
- DSU_JQUERY_URL by default is 'https://code.jquery.com/jquery-3.1.1.min.js', if you want define a custom path to you jquery, so, you can use this template tag.
```python
# settings.py
DSU_JQUERY_URL = '...your jquery path...'
```

## Uninstall django-semantic-ui
- You can uninstall Semantic UI Framework and Gulp (local version) using the follow command:
```shell
$ python manage.py semantic_ui uninstall && pip uninstall django-semantic-ui
```

## Releases notes:

- 1.0.0: Initial and beta version (only installation and settings).
- 1.0.1: Bugs fixed semantic folder not found or not exists.
- 1.0.2: Bugs fixed semantid and static folders not found or not exists.
- 1.0.3: README.md file updated, bugs fixed self.semantic_ui_version undefined.
- 1.1.0: Logic updated to install / uninstall django-semantic-ui, new settings added.
- 1.1.1: Bugs fixed related with the semantic files path.
- 1.1.2: README.md updated
- 1.2.0: New templatetags added to load the main javascripts, stylesheets and jquery_url
- 1.2.1: Bugs fixed using the DSU_JQUERY_URL settings.
- 1.2.2: README.md updated, New static method added to load the STATIC_URL from django project.
