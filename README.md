ZOSIA on OpenShift
===================

The Django project name used in this repo
is `zosiaproject` and is located in wsgi dir.

On subsequent pushes, a `python manage.py migrate` is executed to make
sure that any models you added are created in the DB.  If you do
anything that requires an alter table, make sure to back up your
database w/ `rhc app snapshot save` first :)

You can also turn on the DEBUG mode for Django application using the
`rhc env set DEBUG=True --app $appname`. If you do this, you'll get
nicely formatted error pages in browser for HTTP 500 errors.

Do not forget to turn this environment variable off and fully restart
the application when you finish:

    $ rhc env unset DEBUG
    $ rhc app stop && rhc app start

Setting up the website
----------------------

Create an account at https://www.openshift.com

Install the RHC client tools if you have not already done so:
    
    $ sudo gem install rhc
    $ rhc setup

Create a python application with Postgres cartridge

    $ rhc app create $appname python-3.3
    $ rhc cartridge add postgresql-9.2 -a $appname

Add this upstream repo

    $ cd $appname
    $ git remote add upstream -m master https://github.com/kamarkiewicz/zosiaproject.git
    $ git pull -s recursive -X theirs upstream master

Then push the repo upstream

    git push

Now, you have to create [admin account](#admin-user-name-and-password), so you 
can setup your Django instance.
	
That's it. You can now checkout your application at:

    http://$appname-$yournamespace.rhcloud.com

Admin user name and password
----------------------------
Use `rhc ssh` to log into python gear and run this command:

	python $OPENSHIFT_REPO_DIR/wsgi/zosiaproject/manage.py createsuperuser

You should be now able to login at:
    http://django-$yournamespace.rhcloud.com/admin/

Site requirements
-----------------
In your admin panel go to `Common >> zosiadefinition` and add an entry which prescribes
ZOSIA event. It is essential for this site.

Database backups
----------------

By default, backups are created on file.
To send them to [Dropbox](http://www.dropbox.com):
    1. Create new application at https://www.dropbox.com/developers/apps and set following environment variables:
        ```
        DBBACKUP_DROPBOX_APP_KEY = '<dropbox_app_key>'
        DBBACKUP_DROPBOX_APP_SECRET = '<dropbox_app_secret>'
        ```
    2. Customize `settings.py`:
       * Add
        ```
        TOKENS_FILEPATH = os.path.join(DATA_DIR, 'tokens')
        DBBACKUP_STORAGE = 'dbbackup.storage.dropbox_storage'
        DBBACKUP_TOKENS_FILEPATH = TOKENS_FILEPATH
        DBBACKUP_DROPBOX_APP_KEY = os.environ.get('DBBACKUP_DROPBOX_APP_KEY')
        DBBACKUP_DROPBOX_APP_SECRET = os.environ.get('DBBACKUP_DROPBOX_APP_SECRET')
        ```
        * Delete
        ```
        BACKUP_DIR = os.path.join(DATA_DIR, 'backups')
        DBBACKUP_STORAGE = 'dbbackup.storage.dropbox_storage'
        DBBACKUP_STORAGE = 'dbbackup.storage.filesystem_storage'
        DBBACKUP_STORAGE_OPTIONS = {'location': BACKUP_DIR}
        ```

__DISCLAIMER__ as of Dropbox v3.38 this doesn't work. OAuth flow is broken in SDK.

If you enable cron job, emails will also be sent periodically to email address contained in `DBBACKUP_EMAIL_RECIPIENT` env variable.
