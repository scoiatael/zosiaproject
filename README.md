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

	http://$appname-$yournamespace.rhcloud.com/admin/

Site requirements
-----------------
In your admin panel go to `Common >> zosiadefinition` and add an entry which prescribes
ZOSIA event. It is essential for this site.
