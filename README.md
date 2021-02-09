- [Install Django](#install-django)
    + [.gitignore](#gitignore)
    + [run initial migrations](#run-initial-migrations)
    + [create superuser](#create-superuser)
    + [First commit to github](#first-commit-to-github)
- [Authentication system](#authentication-system)
  * [settings.py](#settingspy)
  * [urls.py](#urlspy)
  * [Added new apps, need to migrate](#added-new-apps--need-to-migrate)
  * [Runserver, with admin](#runserver--with-admin)
  * [Additional settings.py](#additional-settingspy)
    + [With 'allauth' working, need to set up requirements.txt.](#with--allauth--working--need-to-set-up-requirementstxt)
  * [Set up Templates](#set-up-templates)
  * [git](#git)
- [Base Templates](#base-templates)
  * [Create base.html in /templates](#create-basehtml-in--templates)
  * [Create home app.](#create-home-app)
    + [index.html](#indexhtml)
    + [home/views.py](#home-viewspy)
    + [home/urls.py](#home-urlspy)
    + [project level boutique_ado/urls.py](#project-level-boutique-ado-urlspy)
    + [project level boutique_ado/settings.py](#project-level-boutique-ado-settingspy)
    + [Wire up templates directory to settings.py](#wire-up-templates-directory-to-settingspy)
    + [runserver error](#runserver-error)
    + [JSON formatter](#json-formatter)
  * [Fixtures](#fixtures)
  * [Customise Products admin](#customise-products-admin)
    + [products/models.py](#products-modelspy)
    + [products/admin.py](#products-adminpy)
  * [Set up Product views](#set-up-product-views)
    + [Queries](#queries)
    + [Specific categories of products](#specific-categories-of-products)
    + [Sorting](#sorting)
  * [Shopping Bag](#shopping-bag)
  * [Context Processors](#context-processors)
    + [Adding products to shopping bag](#adding-products-to-shopping-bag)
  * [Toasts](#toasts)
  * [checkout app and STRIPE](#checkout-app-and-stripe)
    + [models](#models)
    + [signals](#signals)
    + [checkout form](#checkout-form)
- [Gitpod Reminders](#gitpod-reminders)
- [Updates Since The Instructional Video](#updates-since-the-instructional-video)


<small><i>[TOC](http://ecotrust-canada.github.io/markdown-toc/)</i></small>

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Mike Green,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use.

## Install Django

```pip3 install django```

>Collecting django
  Downloading Django-3.1.5-py3-none-any.whl (7.8 MB)
     |████████████████████████████████| 7.8 MB 9.3 MB/s 
Collecting asgiref<4,>=3.2.10
  Downloading asgiref-3.3.1-py3-none-any.whl (19 kB)
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.4.1-py3-none-any.whl (42 kB)
     |████████████████████████████████| 42 kB 2.0 MB/s 
Collecting pytz
  Downloading pytz-2020.5-py2.py3-none-any.whl (510 kB)
     |████████████████████████████████| 510 kB 83.8 MB/s 
Installing collected packages: sqlparse, pytz, asgiref, django
Successfully installed asgiref-3.3.1 django-3.1.5 pytz-2020.5 sqlparse-0.4.1
WARNING: You are using pip version 20.3.3; however, version 21.0 is available.
You should consider upgrading via the '/home/gitpod/.pyenv/versions/3.8.7/bin/python3 -m pip install --upgrade pip' command.

```django-admin startproject boutique_ado . ```

- ![start project directories](/boutique_ado/static/docs/start_project.jpg)


#### .gitignore
- core.Microsoft*
- core.mongo*
- core.python*
- env.py
- __pycache__/
- *.py[cod]
- *.sqlite3

``` python3 manage.py runserver ```

>Watching for file changes with StatReloader
Performing system checks...

>System check identified no issues (0 silenced).

>You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
January 23, 2021 - 16:55:30
Django version 3.1.5, using settings 'boutique_ado.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

#### run initial migrations

```python3 manage.py migrate```

#### create superuser

``` python3 manage.py createsuperuser ```

username: mdjg
email address: 
password:

#### First commit to github

```git remote -v```

>origin  https://github.com/mikedjgreen/MSP4_demo.git (fetch)
origin  https://github.com/mikedjgreen/MSP4_demo.git (push)

## Authentication system

```pip3 install django-allauth```

...

>Successfully built django-allauth
Installing collected packages: pyjwt, oauthlib, requests-oauthlib, python3-openid, django-allauth
Successfully installed django-allauth-0.44.0 oauthlib-3.1.0 pyjwt-2.0.1 python3-openid-3.2.0 requests-oauthlib-1.3.0

[Allauth documentation](https://django-allauth.readthedocs.io/en/latest/installation.html)

### settings.py
Need to add allauth entries to the settings.py .

INSTALLED_APPS

-    'django.contrib.sites',

-    'allauth',
-    'allauth.account',
-    'allauth.socialaccount',

After AUTHENTICATION_BACKENDS:

```SITE_ID = 1```

### urls.py

```from django.urls import path, include```

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]

### Added new apps, need to migrate

```python3 manage.py migrate```

>Operations to perform:
  Apply all migrations: account, admin, auth, contenttypes, sessions, sites, socialaccount
Running migrations:
  Applying account.0001_initial... OK
  Applying account.0002_email_max_length... OK
  Applying sites.0001_initial... OK
  Applying sites.0002_alter_domain_unique... OK
  Applying socialaccount.0001_initial... OK
  Applying socialaccount.0002_token_max_lengths... OK
  Applying socialaccount.0003_extra_data_default_dict... OK

### Runserver, with admin

```python3 manage.py runserver```

This gives a 404 error, but append /admin to URL to get:

- ![admin login](/boutique_ado/static/docs/admin_login.jpg)

Login with mdjg.

- ![mdjg logged in](/boutique_ado/static/docs/mdjg_logged_in.jpg)

Alter site to boutiqueado.example.com.

### Additional settings.py

Temporarily log emails to console to get the confirmation links.

``` 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
```
```
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/##success##'
```

##success## is temporary setting to test.
Test this with:
``` python3 manage.py runserver ```

Get Page not found (404).

Navigate to ```/accounts/login``` at the end of the url.  


Get: 
- ![accounts login](/boutique_ado/static/docs/accounts_login.jpg)

The superuser was setup prior to installing allauth, so an email has not been associated with this login.

Can set this for 'mdjg' by logging into admin.

Need to set accounts' email addresses, and search for account mdjg.
Add an email address and tick verify.

- ![add email address](/boutique_ado/static/docs/add_email_addr.jpg)



#### With 'allauth' working, need to set up requirements.txt.

```pip3 freeze > requirements.txt ```

- asgiref==3.3.1
- Django==3.1.5
- django-allauth==0.44.0
- oauthlib==3.1.0
- PyJWT==2.0.1
- python3-openid==3.2.0
- pytz==2020.5
- requests-oauthlib==1.3.0
- sqlparse==0.4.1

### Set up Templates

``` mkdir templates ```

``` mkdir templates/allauth```

### git

``` git add .```

``` git commit -m "Setup allauth" ```

``` git push ```

## Base Templates

At some point we will want to customise the allauth templates within our templates\allauth directory.

pip3 installs files such as allauth in the site-packages directories.

```pwd   returns /workspace/MSP4_demo```

This is also env $THEIA_WORKSPACE_ROOT


```cd ..```

```ls -la  ```

returns 
>
- drwxr-xr-x 2 gitpod gitpod 4096 Jan 25 12:45 .gitpod
- -drwxr-x--- 6 gitpod gitpod 4096 Jan 24 16:42 MSP4_demo
-d rwxr-x--- 6 gitpod gitpod 4096 Jan 25 12:45 mysql
- drwxr-xr-x 4 gitpod gitpod 4096 Jan 23 16:41 .pip-modules
>

```cd .pip-modules```
```cd lib```
```cd python3.8```
```cd site-packages```
```ls -la```
returns

>
- drwxr-xr-x  8 gitpod gitpod 4096 Jan 23 17:28 openid
- drwxr-xr-x  2 gitpod gitpod 4096 Jan 23 17:28 PyJWT-2.0.1.dist-info
- drwxr-xr-x  2 gitpod gitpod 4096 Jan 23 17:28 python3_openid-3.2.0.dist-info
- drwxr-xr-x  4 gitpod gitpod 4096 Jan 23 16:41 pytz
- drwxr-xr-x  2 gitpod gitpod 4096 Jan 23 16:41 pytz-2020.5.dist-info
- drwxr-xr-x  4 gitpod gitpod 4096 Jan 23 17:28 requests_oauthlib
- drwxr-xr-x  2 gitpod gitpod 4096 Jan 23 17:28 requests_oauthlib-1.3.0.dist-info
- drwxr-xr-x  5 gitpod gitpod 4096 Jan 23 16:41 sqlparse
- drwxr-xr-x  2 gitpod gitpod 4096 Jan 23 16:41 sqlparse-0.4.1.dist-info
>

**but no allauth/templates directory as course vid states ????**

- From Slack: [allauth source](https://github.com/pennersr/django-allauth)

### Create base.html in /templates

Getting most of the boilerplate from bootstrap.

- [Bootstrap](https://getbootstrap.com/)

Copy [starter template](https://getbootstrap.com/docs/4.4/getting-started/introduction/#starter-template) from bootstrap's docs page onto base.html.

Adding {% blocks %} as needed.

### Create home app.

```python3 manage.py startapp home```

- ![startapp home](/boutique_ado/static/docs/startapp_home.jpg)

```mkdir home/templates```

```mkdir home/templates/home```

```touch home/templates/home/index.html``` 

#### index.html

```
{% extends "base.html" %}
{% load static %}

{% block content %}
    <h1 class="display-4 text-success">It works!</h1>
{% endblock %}
```

#### home/views.py

```
from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
```

#### home/urls.py

Create file (startapp does not create it).

```
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home')
]
```


#### project level boutique_ado/urls.py

Add the line:
``` path('', include('home.urls')),```

#### project level boutique_ado/settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'home'
]
```

#### Wire up templates directory to settings.py

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
```

#### runserver error

``` python3 manage.py runserver ```
gives:

```TemplateDoesNotExist at /```

In your settings.py, the template directory should be relative to root dir. Replace this line:

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
```

...with:

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
```

..Or:

```
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
```

#### JSON formatter
- [JSON formatter](https://jsonformatter.org/)


### Fixtures

```
gitpod /workspace/MSP4_demo $ python3 manage.py loaddata categories
BASE_DIR: /workspace/MSP4_demo
2 BASE_DIR: /workspace/MSP4_demo/boutique_ado
/workspace/MSP4_demo/boutique_ado/media
Installed 9 object(s) from 1 fixture(s)
gitpod /workspace/MSP4_demo $ python3 manage.py loaddata products
BASE_DIR: /workspace/MSP4_demo
2 BASE_DIR: /workspace/MSP4_demo/boutique_ado
/workspace/MSP4_demo/boutique_ado/media
Installed 172 object(s) from 1 fixture(s)
```

### Customise Products admin

#### products/models.py

```
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
```

#### products/admin.py

2 new classes: 
1) class ProductAdmin(admin.ModelAdmin)

```
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)
```
2) class CategoryAdmin(admin.ModelAdmin)

```
    list_display = (
        'friendly_name',
        'name',
    )
```

### Set up Product views

Products/views.py

Products/products.html


```[../boutique_ado$] mkdir -p products/templates/products ```

#### Queries

See Django [query documentation.](https://docs.djangoproject.com/en/3.1/topics/db/queries/).

In products/views.py:

```
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
from django.contrib import messages
from django.db.models import Q
```
Further down the code:
``` 
query = None  

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }
```

####  Specific categories of products

includes/main-nav.html:

```
    <a href="{% url 'products' %}?category=activewear,essentials" class="dropdown-item">Activewear &amp; Essentials</a>
    <a href="{% url 'products' %}?category=jeans" class="dropdown-item">Jeans</a>
    <a href="{% url 'products' %}?category=shirts" class="dropdown-item">Shirts</a>
    <a href="{% url 'products' %}?category=activewear,essentials,jeans,shirts" class="dropdown-item">All Clothing</a>
```

products/views.py:

```
 if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

```

#### Sorting

products/views.py:

```
    sort = None
    direction = None
```
further down:

```
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

```

includes/main-nav.html:

```
    <a href="{% url 'products' %}?sort=price&direction=asc" class="dropdown-item">By Price</a>
    <a href="{% url 'products' %}?sort=rating&direction=desc" class="dropdown-item ">By Rating</a>
    <a href="{% url 'products' %}?sort=category&direction=asc" class="dropdown-item ">By Category</a>
```
### Shopping Bag

1) Creating new app called bag.

``` python3 manage.py startapp bag ```

2) Adding app to settings.py, 'INSTALLED_APPS'.

3) Creating bag/views.py (using home/views.py as template):
```
from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')
```

4) Creating '/workspace/MSP4_demo/bag/templates/bag' directory.

5) Create 'bag.html' within templates/bag diretory, using home/index.html.

6) Create bag/urls.py using home/urls.py as template.
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag')
]
```

7) Include bag urls in project level boutique_ado/urls.py

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
```


8) base.html add link to bag.
```
 <a class="{% if grand_total %}text-info font-weight-bold{% else %}text-black{% endif %} nav-link" href="{% url 'view_bag' %}">
```

9) add link to mobile version of top header,  templates/includes/mobile-top-header.html.

"{% url 'view_bag' %}"


### Context Processors

This will return a dictionary called context that keeps track of the contents of the shopping bag.
This can be viewed by all apps.

1) Create bag/contexts.py

Within this will be a function called bag_contents.
```

from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
```

2) To make contexts.py available to all, need to add to settings.py
``` 'context_processors': [ ```

``` 'bag.contexts.bag_contents',  # for shopping bag ```


#### Adding products to shopping bag


### Toasts 

### checkout app and STRIPE 

``` python3 manage.py startapp checkout```

settings.py :

```
INSTALLED_APPS [
...
    'bag',
    'checkout',
]
```

#### models 

checkout/models.py :

#### signals 

checkout/signals.py :

#### checkout form 






## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.


