#!/bin/bash

# Update NGINX config
#TODO: test before symlink (ln -s)
cp /srv/$TEMPLATENAME/infra/apis.$TEMPLATENAME.conf /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/apis.$TEMPLATENAME.conf /etc/nginx/sites-enabled/
cp /srv/$TEMPLATENAME/infra/$TEMPLATENAME.conf /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/$TEMPLATENAME.conf /etc/nginx/sites-enabled/
cp /srv/$TEMPLATENAME/infra/upstream_$TEMPLATENAME.conf /etc/nginx/conf.d/
service nginx restart

# Update gunicorn and supervisor
cp /srv/$TEMPLATENAME/infra/gunicorn_$TEMPLATENAME.conf /etc/supervisor/conf.d/
supervisorctl reread
supervisorctl restart $TEMPLATENAME:gunicorn
