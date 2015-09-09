ZOSIA on OpenShift
===================

The Django project name used in this repo
is 'zosiaproject' and is located in wsgi dir.  Right now the
backend is sqlite3 and the database runtime is found in
`$OPENSHIFT_DATA_DIR/db.sqlite3`.

On subsequent pushes, a `python manage.py migrate` is executed to make
sure that any models you added are created in the DB.  If you do
anything that requires an alter table, you could add the alter
statements in `GIT_ROOT/.openshift/action_hooks/alter.sql` and then use
`GIT_ROOT/.openshift/action_hooks/deploy` to execute that script (make
sure to back up your database w/ `rhc app snapshot save` first :) )

You can also turn on the DEBUG mode for Django application using the
`rhc env set DEBUG=True --app APP_NAME`. If you do this, you'll get
nicely formatted error pages in browser for HTTP 500 errors.

Do not forget to turn this environment variable off and fully restart
the application when you finish:

```
$ rhc env unset DEBUG
$ rhc app stop && rhc app start
```

Running on OpenShift
--------------------

Create an account at https://www.openshift.com

Install the RHC client tools if you have not already done so:
    
    sudo gem install rhc
    rhc setup

Create a python application

    rhc app create django python-3.3

Add this upstream repo

    cd django
    git remote add upstream -m master https://github.com/kamarkiewicz/zosiaproject.git
    git pull -s recursive -X theirs upstream master

Then push the repo upstream

    git push

Now, you have to create [admin account](#admin-user-name-and-password), so you 
can setup your Django instance.
	
That's it. You can now checkout your application at:

    http://django-$yournamespace.rhcloud.com

Admin user name and password
----------------------------
Use `rhc ssh` to log into python gear and run this command:

	python $OPENSHIFT_REPO_DIR/wsgi/zosiaproject/manage.py createsuperuser

You should be now able to login at:

	http://django-$yournamespace.rhcloud.com/admin/
