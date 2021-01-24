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


