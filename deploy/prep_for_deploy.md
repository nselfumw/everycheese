### Restarting

If you stop your terminal session and need to restart you probably need to run two commands first:
```
source ~/.venvs/django/bin/activate  
export DJANGO\_SETTINGS\_MODULE=config.settings.production
```
### Set up DNS

*   Log into Domain of One's Own: [https://umw.domains/dooo/dashboard/](https://umw.domains/dooo/dashboard/)
*   Go to Zone Editor
*   Add A Record
*   Enter only the subdomain you want, it will supply the rest. For instance enter "everycheese" to create a record for everycheese.selfontheinter.net
*   Enter the IP address of the CPSC server 35.209.0.91
*   Check if it's working with ping everycheese.selfontheinter.net (will take a few minutes for DNS to propagate)

### Change production.py

*   comment out caches section
*   comment out mailgun section
*   add WHITENOISE_MANIFEST_STRICT = False
    * This tells your project to return 404s if your code requests a non-existent static file. Without this, it will raise a server error

### Change requirements/production.txt

*   Replace pyscopg with mysqlclient==2.2.4

### Clone to server

*   Push changes to GitHub
*   Clone onto server
*   Use https to clone but if you can't then you need to make ssh keys on the CPSC server
*   [Docs to make ssh keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key "Link")

### Make virtualenv
```
mkdir ~/.venvs  
python3.10 -m venv ~/.venvs/django  
source ~/.venvs/django/bin/activate
```
### Install dependencies
```
pip install wheel  
pip install -r requirements/production.txt
```
### Make .env file for secrets

*   at root of repository, change database\_url and allowed\_hosts to your values
*   format of database\_url is mariadb://<databaseUserName>:<databasePassword>@localhost/<databaseName>
```
DJANGO_SECRET_KEY=manyrandomlettersandnumbershere  
DATABASE_URL=mysql://nself:password@localhost/nself  
DJANGO_ADMIN_URL=notthewordadmin  
DJANGO_ALLOWED_HOSTS=everycheese.selfontheinter.net
```

### Initialize database
```
export DJANGO_SETTINGS_MODULE=config.settings.production  
./manage.py migrate  
./manage.py collectstatic  
./manage.py createsuperuser
```

Use actual, strong password for admin here. It's open to the internet.

### Write apache config

[https://github.com/nselfumw/everycheese/blob/main/deploy/apache.conf](https://github.com/nselfumw/everycheese/blob/main/deploy/apache.conf)

Put it in the deploy directory in your repo. Changes to make (possibly via find/replace):

1.  Domain name
2.  Absolute path to your repository on the CPSC server
3.  Pick a unique WSGI name (maybe made up of your username and your project name)
4.  python-home directory

### Submit path to apache config

**Submit the absolute path to your apache config to this assignment**. You can get this (if your shell is in the same directory as the apache config file) with:

```
realpath apache.conf
```
