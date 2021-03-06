# Settings for Django testcases against kobo hub
import os

KOBO_DIR = os.path.normpath(
    os.path.join(os.path.dirname(__file__), '..', 'kobo')
)

SECRET_KEY = "key"
XMLRPC_METHODS = []
TASK_DIR = '/tmp/kobo-test-tasks'
UPLOAD_DIR = '/tmp/kobo-test-dir'

# The middleware and apps below are the bare minimum required
# to let kobo.hub load successfully

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'kobo.django.auth.middleware.LimitedRemoteUserMiddleware',
    'kobo.hub.middleware.WorkerMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'kobo.django',
    'kobo.hub',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'testdatabase',
    }
}

# We need to specify the template dirs because:
# - the admin/templates don't belong to a particular django app, instead
#   they're intended to be copied to another app by a custom command, but
#   we don't want to run that during the tests
# - automatic lookup of templates under kobo/hub isn't working for some reason,
#   not sure why, but might be related to use of deprecated arguments in
#   render_to_string (FIXME)
TEMPLATE_DIRS = (
    os.path.join(KOBO_DIR, 'admin/templates/hub/templates'),
    os.path.join(KOBO_DIR, 'hub/templates'),
)

ROOT_URLCONF = 'tests.hub_urls'
