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

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

--------

Happy coding!
