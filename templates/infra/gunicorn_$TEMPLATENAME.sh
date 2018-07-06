#!/bin/bash

# TODO: get from Environment variables
NAME="$TEMPLATENAME"                                  # Name of the application
DJANGODIR=/srv/$TEMPLATENAME/apis             # Django project directory
SOCKFILE=/srv/$TEMPLATENAME/infra/$TEMPLATENAME_apis.sock  # we will communicte using this unix socket
USER=$TEMPLATENAME                                        # the user to run as
GROUP=www-data                                     # the group to run as
NUM_WORKERS=4                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=$TEMPLATENAME.settings.prod             # which settings file should Django use
DJANGO_WSGI_MODULE=$TEMPLATENAME.wsgi                     # WSGI module name
DB_PWD=password

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /srv/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export $TEMPLATENAME_DB_PWD=$DB_PWD
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
echo "Python path: $PYTHONPATH"
export PYTHONPATH=$DJANGODIR:/srv/venv/bin

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /srv/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=/var/log/$TEMPLATENAME/gunicorn.log
