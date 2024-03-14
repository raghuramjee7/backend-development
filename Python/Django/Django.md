# Learning Django

## Virtual Environments
Virtual environments help us in setting up a closed environment to install all the necessary packages. We use the *venv* module for this.  
**Create a new virtual environment** - `python -m venv <venv_name>`  
This created a hidden .venv folder in the directory  
**Activate the virtual environment** - `<venv_name>\Scripts\Activate.ps1`  
**Deactivate the virtual environment** - `deactivate`

### Other Steps
1. Create a `.gitignore` file and put *.venv* and *.gitignore* files in it, other files as well, which you wouldn't want to commit
2. **Generate a requirements file** - `pip freeze > requirements.txt`  
  
After setting up the virtual environment we can install all the packages that we want using `pip`.
**Install a Package** - `python -m pip install django~=4.0.0`  
We provide the version to install to avoid any dependency clashes  


## Starting a Django Project  
**Start a Django Project** - `django-admin startproject <project_name> .`  
We add the (.) at the end for the folder structure. If we dont put a (.), it creates an outer folder with the same name as project name and puts all the files inside this. With the (.) it just creates inside the folder with venv.  
### Structure
├── django_project   
│ ├── \_\_init\_\_.py  
│ ├── asgi.py  
│ ├── settings.py  
│ ├── urls.py  
│ └── wsgi.py  
├── manage.py  
└── .venv/  

For local deployment we can use internal web server, but later, we would use a more sophisticated web server like *Gunicorn*. 
**Run server in local** - `python manage.py runserver`  
**Stop server in local** - `CTRL+C`  
At the first run, we see a warning for migrations, this is just to setup the database for the project. The server is hosted at *http://127.0.0.1:8000/*  

### Files in the project  
1. **\_\_init\_\_.py**  - Just to refer that the project is a package so we can files and classes from here.  
2. **asgi.py** - It allows the *Asynchronous Server Gateway Interface* to be run.  
3. **settings.py** - Controls the overall settings of the project.  
4. **urls.py** - To configure urls for the project.  
5. **manage.py** - It is not a part of the project but is used to execute various commands, for eg - runserver.  

**Migrate the Database** - `python manage.py migrate`  
This creates a new db.sqlite3 file to store our data. 

### HTTP Request Response Cycle  
The user sends a request to the server and the server responds with a response. This is the cycle.  
**Flow in Django** -  
HTTP Request -> URL -> Django combines database, logic, styling ->
HTTP Response 
#### MVC vs MVT 
*Model-View-Controller* pattern seperates the data, logic and display of application into various components. 
1. *Model*: Manages data and core business logic  
2. *View*: Renders data from the model in a particular format  
3. *Controller*: Accepts user input and performs application-specific logic  

Django follows an updated version of MVC called MVT - Model-View-Template. Actually, Django follows a deeper approach called MVTU - Model-View-Template-URL Configuration.  
1. *Model*: Manages data and core business logic  
2. *View*: Describes which data is sent to the user but not its presentation  
3. *Template*: Presents the data as HTML with optional CSS, JavaScript, and Static Assets  
4. *URL Configuration*: Regular-expression components configured to a View  

### Django RR Cycle
HTTP Request -> URL -> View -> Model and Template -> HTTP Response  
Django finds the URL in urls.py. Each URL is mapped to a single view and django goes to this view. Here, it combines data from the model and styling from the template and the response is sent to the user.  

## Django App  
A project can contain multiple apps. Each app takes care of one single functionality, like authentication, payments etc.  
**Start an app** - `python manage.py startapp <app_name>`  
**App Structure** -   
├── APP  
│ ├── \_\_init\_\_.py  
│ ├── admin.py  
│ ├── apps.py  
│ ├── migrations  
│ │ └── \_\_init\_\_.py  
│ ├── models.py  
│ ├── tests.py  
│ └── views.py  
Let us take a look at each file in the app  
1. *\_\_init\_\_.py* - used to make it a package  
2. *admin.py* - Configuration file for already built-in Admin App  
3. *apps.py* - Configuration file for the app itself
4. *migration/* - This folder keeps the track of all the changes in the database so that models.py stays up to date. 
5. *models.py* - Defines the database model for the app  
6. *tests.py* - Used to write tests for the app 
7. *views.py* - Defines views for RR cycle  

Once after creating the app, we need to add the app to the Django Project.   
`Open <project_name>/settings.py file, find INSTALLED_APPS list variable and add appName.apps.AppConfig to it` 

### Views
In Django, there are two types of views - *Class Based Views* and *Function Based Views*.  
Class Based Views allows us to have greater code reusability, and Django has some internal built-in views called *Generic Class Based Views*

### URLs
1. We need to create our own *urls.py* file in the app. Here, all the urls for an app are added.
2. Import path from django.urls and the views you want to import.
3. Create a list variable called `urlpatterns` and add each url path

```
path("<regex_pattern>", <view_name>, name=<named_url_pattern>)
```
Named URL Patterns help us in naming the url, so instead of remembering the path for every url, we can get the url from the named url pattern. This is used in jinja syntax as well as we can get the url from the `reverse()` function.  
Now, we need to update the `urls.py` file in project level for it to recognise the app urls, so add the path in its `urlpatterns` variable
```
path(<path_name>, include("AppName.urls"))
```

### Templates
Templates are individual html files that can be rendered from a response. These are stored in *templates/* folder. There are two options in django to put the templates folder.  
1. We can have an individual templates folder inside each app. App/ -> templates/ -> App/ -> template.html
2. We can have a single project level *templates/* folder and update the *settings.py* file  

Create a templates folder parallel to project folder `mkdir templates`.  
Update *TEMPLATES* folder in *settings.py* 
```
TEMPLATES = [
    {
        'DIRS': [BASE_DIR/"templates"],
    }
]
```
Create a new html file in the folder. 
To Link Templates - `"{% url '<url_name>' %}"`

### Views
In *views.py* file of each app, we create different classes for each view. These views are inherited from some built-in views and we use these to bind everything.  
```
from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = "home.html"
```
Use the `ViewName.as_view()` in the `path()` function for URLs.

### Template Inheritance
We can extend the templates in django, this helps us in creating default headers and footers. We use Jinja syntaxing for different things -> loops, urls, inheritance, etc.
To set URL in webpage -  
```
<a href="{% url '<named_url_convention>' %}">Home</a> 
```
We can created a block of code to be inherited by 
```
{% block <block_name> %} {% endblock <block_name> %}
```
Here, the block_name is used for inheritance, the code upper to it will be inherited and this part will be variable.  
To extend a template, we use
```
{% extends "base.html" %}
{% block content %}
//code
{% endblock content %}
```
We can have a *base.html* file that contains the main code and others can inherit from it.  

## Testing
Testing is divided into 2 main categories  
1. **Unit Testing** - Check a piece of individual function that is isolated.  
2. **Integration Testing** - This checks multiple pieces that are binded together. 

Unit tests are faster and simpler. It is better to write many unit tests and less integration tests.  
Python has an internal `unitttest` module that uses `TestCase` instances and `assert` statements to check for trueness. This unittest library is based on the JUnit testing framework in Java.  
Django has its own testing framework on top of python's unittest module. It also creates a dummy web client to make requests. There are several useful classes in it.  
1. **SimpleTestCase** - When no database is necessary
2. **TestCase** - When database is necessary
3. **TransactionTestCase** - Test live database transactions
4. **LiveServerTestCase** - Launches live server thread to test with selenium  

These tests go in the *tests.py* file.  
To run the tests - `python manage.py test`  
**Sample Testing Code**  
```
from django.test import SimpleTestCase
from django.urls import reverse

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
    def test_template_name_correct(self): # new
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
    def test_template_content(self): # new
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Homepage</h1>")

class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
    def test_template_name_correct(self): # new
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")
    def test_template_content(self): # new
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About page</h1>")
``` 

## Models

Django has an ORM (Object Relational Mapper) that can translate what we write in *models.py* into different query languages. Django by default uses SQLite database. We only need to configure *settings.py* file to update the database.  
**Sample Model** - 
```
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
                    "auth.User",
                    on_delete=models.CASCADE,
                    )
    body = models.TextField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
```
`get_absolute_url()` function gets the url with the primary key.  
We can also setup foreign keys for n:1 relationships

Now, whenever we create a new model or update an old model, there is a 2 step process
1. Create a migrations file with `python manage.py makemigrations <app_name>`. This is a file to reference all the changes made in the database. We can track changes through this. If we dont specify the app name, this will be run for all the apps in the project.  
2. Run the `python manage.py migrate` command to run the actual migration.

### Django Admin
Django has a pre built admin interface that helps us in keeping track of the DB. We just need to create a superuser for it.
**Create SuperUser** - `python manage.py createsuperuser`  
Go to `localhost:8000/admin` to check admin interface.  

We dont see our model initially because we didnt register it. Go to *admin.py* file in the app and register the model.  
```
admin.site.register(Key)
```

We can use `ListView` to connect both DB as well as Template.  
```
class HomePageView(ListView):
    model = <model_name>
    template_name = "<template_name>"
```

We can convert our model(db) into a list very simply. We can use `<model>_list`   
**For Loop in Jinja**  
```
{% for post in post_list %}
    <li>{{ post.text }}</li>
{% endfor %}
```


## Static Files
All the CSS, JS, Image files are stored in a *static/* folder. Similar to template folder, django looks for app level static/ folder. Instead of this, we can always set up the templates/ earlier. 
We need to update *settings.py* file so that it can locate the static/ folder.  
Add the following to *settings.py* file  
```
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
```
Create a seperate folder called `css/` inside to place CSS files.  
Attach the css file to html -
```
{% load static %}
<link rel="stylesheet" href="{% static 'css/<file_name>.css' %}">
```
We can use `DetailView` GCBV to look at data. We pass the primary key of the data to look at that particular data item.This is called the **context object** When we pass the object through its primary key, we can access that object in two ways 
1. Through `<model>` name in lowecase
2. Through the `object` keyword.  
To access these context object, we access it through url, and we put the primary key even in the url as well like `"path/<int:pk>/"`, Here <int> is the datatype and `pk` is the primary key.  
This primary key is an autoincrementing field that django defines in the db model. We can access this either by `id` or `pk`.  

## Forms
We can handle forms with different GCBV. We have CreateView, UpdateView, DeleteView.   
```
class ViewName(CreateView):
    model = <model_name>
    template_name = "<template_name>"
    fields = ["<field1>", "<field2>", ..]
```
The fields that we mention are the fields that we want to expose in the form.  
Now the form looks like this -  
```
<form action="" method="post">
{% csrf_token %}
{{ form.as_p }}
</form>
```
Here the csrf_token is to prevent cross-site request forgery.   
The form.as_p, puts each of the field in a paragraph, so we dont need to fill the input forms.  
For DeleteView, we also have a successurl, which is the url it redirects to after a succesful delete.   
`success_url = reverse_lazy("home")`  
Here, we use reverse_lazy instead of reverse because, it waits till the deletion happens and after that, it redirects. For Create and Update views, it by default access the get_absolute_url function, so it basically redirects to the update page. 

## Django User
Django has a built in user authentication module and a predefined user for us.  
When a new app is created, Django installs the `auth` app, which creates a user object with -
1. username
2. password
3. email
4. first name
5. last name

### Login
We have all the views required for it - LoginView which is by default present. We need to do some steps before it  
1. Add a url pattern for auth system
2. A Login/SignUp template under registration folder
3. Update *settings.py* file to setup login redirect

#### Add URL pattern in project 
```
path("accounts/", include("django.contrib.auth.urls"))
```
#### Create Login File
For LoginView to work, Django looks for a file called `login.html` in the templates folder under `registration` directory. So, we need to create a registration/ folder under templates. We dont need any additional new view to be created, we can directly write the html file with the form. 

#### Redirect Login with Settings.py
After a successful login,, we need to define where the app needs to be redirected. This is pretty simple.
```
LOGIN_REDIRECT_URL = "<named_url_convention>" 
```
To check if a particular user is authenticated or not, we use the `user.is_authenticated` variable. This can be used in if-else blocks. 
The url for logout is `logout`. Similar to login redirect url, we have logout redirect url
```
LOGOUT_REDIRECT_URL = "<named_url_convention>
```

### SignUp
Unlike login, we need to write our own view for signup, since we need specified fields. However, we can use the `CreateView` and a predefined form called `UserCreationForm` with a variable called `form_class`
For the sake of modularity, we can create a new app for maintaining the accounts. Let this app be `accounts`.  
This app needs to be added to `INSTALLED_APPS`, and the url pattern needs to be added to it. 
The order of searching in project level urls is important, django goes orderwise. So `auth` should go first. First django looks for `accounts/signup` in auth, it doesnt find it there, then it goes to our user defined accounts app.

### Custom User Model
Even after Django providing a base user, it is always better to create a custom user. This needs to be done at the beginning of the project.  

#### Steps for Custom User Model
1. Update *settings.py* file
2. Create new CustomUser Model
3. Create new forms for UserCreationForm and UserChangeForm
4. Update accounts/admin.py

##### Update settings.py file
Add accounts app to installed apps and use AUTH_USER_MODEL config to change the model that is used for authentication from the inbuilt model. 
```
AUTH_USER_MODEL = "accounts.<model_name>" 
```

##### Create CustomUser Model
We will use *AbstractUser* base class to accomplish this. We inherit from this and add all the new fields that we want into it.  
```
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
```
`null` and `blank` are two different fields that we used above.  
Null is database related. It means that the database can have null values.  
Blank is form related. If blank is true, then the form accepts blank values, else it doesnt.  

##### Creating new forms
Forms are one of the way we interact with database. The user signs up or updates his profile. These related forms also need to be updated to add those details. 
We need to create a new file called `forms.py` in accounts app and update the forms there.  

```
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("age",)
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
```
We use the Meta class to override the model it is mapping and the fields it has, all we have to do is to add a new field `age` to append that field to a form. 

##### Updating Admin.py  
Admin.py is tightly related to the default User Model. The `UserAdmin` class is attached to the CustomUser model. There are some variables that need to be set.
1. **list_display** - to control which fields are listed.
2. **fieldsets** - To edit custom fields (for editing users)
3. **add_fieldsets** - To add custom fields (for creating users)  

The code would look - 
```
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
                    "email",
                    "username",
                    "age",
                    "is_staff",
                    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields":
    ("age",)}),)
    admin.site.register(CustomUser, CustomUserAdmin)
```
This sets up the admin model for the project as well.  
Now, we can run makemigrations and migrate in the project. We are all done!

To add the newly added fields to login, signup forms, we need to update the `CustomUserCreationForm` and put the following - 
```class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
        "username",
        "email",
        "age",
        ) 
```

## Static Files
The static files in django are in the static folder, and we setup static_folder_dirs variable, etc. But, Django wont serve static files in production, so there are some extra steps here.
1. Run `python manage.py collectstatic` command to compile all static files into a single directory for deployment. 
2. Set `STATIC_ROOT` configuration, which sets the absolute location of all the static files to a folder called `staticfiles`
3. Setup `STATICFILES_STORAGE`, which is the file storage engine used by `collectstatic`. 
```
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage" 
```
Before deploying into production, `collectstatic` must be run each time.  
These compiled staticfiles can be served using a package called **`WhiteNoise`**. This needs to be installed.  
After installing WhiteNoise, there are some steps to be done.
1. Add it to INSTALLED_APPS - `"whitenoise.runserver_nostatic"`
2. Add it to MIDDLEWARE - `"whitenoise.middleware.WhiteNoiseMiddleware"`
3. Update `STATICFILES_STORAGE` - `"whitenoise.storage.CompressedManifestStaticFilesStorage"`


## Bootstrap
Bootstrap allows us to provide styling to our pages with minimal coding. There are two ways to add bootstrap to our project - 
1. Download all the files and serve them locally
2. Rely on a CDN (Content Delivery Network) 

The second approach is simpler to implement.   
**Steps to add Bootstrap**
1. Add meta name="viewport" at the top within <head>
2. Add Bootstrap CSS link within <head>
3. Add Bootstrap JS bundle at the bottom of body section

The links for CSS and JS are in boostrap website. Immediately after adding Bootstrap, the color of urls and font of the pages changes.  

Using Bootstrap components, we can style the pages as we want. For forms we can use other libraries.  

### Crispy Forms
To display the forms in a neat way, we could use a django library called `django-crispy-forms`.  
To install it, run
```
python -m pip install django-crispy-forms==1.13.0
python -m pip install crispy-bootstrap5==0.6
```
Then add it to the installed apps list - 
```
"crispy_forms",
"crispy_bootstrap5", 
```
Then, at the bottom of the `settings.py` file, we need to add the following lines - 
```
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
```
This concludes the setup, all we need to do now is to use it in forms, for this we need to do 2 things in the html file - 
```
{% load crispy_forms_tags %} - at the start
{{ form|crispy }} - instead of forms.as_p
``` 


## Passwords
Django has an inbuilt password change and reset GCBVs. The steps are -  
1. Create new forms for password update and done in registration/ folder.  
2. For password reset, Django already has a congfiguration. The only thing we need to define is how to send the email. We could use different services like SendGrid to send that particular email. 
3. To add the email as a service, we need to update `settings.py`. 
```
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" 
```
After that we have to go to the following url to update the password - `http://127.0.0.1:8000/accounts/password_reset/`. This provides a form to automatically update a user password.  
We then create 4 new forms in registration folder -
1. password_reset_form - That asks the email id for reset
2. password_reset_done - To say that mail is sent after inputting the email
3. password_reset_confirm - This lets us update the new password
4. password_reset_complete - This confirms that the password has been changed.  

The url for this is - `password_reset`

### Sending emails through services
We can send emails through different services, like sendgrid, etc. It is fairly easy to setup these services. 


## Authentication & Authorization
Now, we can setup some authorizations to only allow a particular set of users to perform a particular set of tasks.  
For eg, if we want to confirm if the user creating an article is a logged in user, then we can add the following piece of code to the View - 
```
def form_valid(self, form): # new
    form.instance.<user_mapping> = self.request.user
    return super().form_valid(form)
```
This way, we can check if the form is valid 

### Mixins
Mixins allow us to add additional functionality over the code, to perform some checks so that, only authorised users can perform some actions, for example - we have `LoginRequiredMixin` which binds a view to a login required condition. This redirects to login page to perform any further action.  
There is another mixin where only the correct user can delete something. This can be done with `UserPassesTestMixin`. This has a `test_func` which needs to pass. We can override this test_func and write our own test and that needs to pass, like - 
```
def test_func(self): # new
    obj = self.get_object()
    return obj.<user_field> == self.request.user
```
Here, the current user is the the user who has access to this table item, ie the current author, user, etc. 
The order of mixins is also important, order them in the way they need to be checked.  

## Extras
We can use inlines in Django Admin to add additional fields to see in admin page. There are two inlines - 
1. TabularInline
2. StackedInline
There is only one difference between the both, in tabular, all fields are displayed in a table row, while in stacked each field has a new row.  
`article.comment_set.all ` This is a simple relation to get all the comments of an article. In the comments model, article id is a foreign key. The `FOO_set` command helps here.   
We can use the **ModelForm** class to convert models into their respective forms. Use the following code in *forms.py* file -
```
class FormName(forms.ModelForm):
    class Meta:
        model = <ModelName>
        fields = ("field1", "field2", ..)
```
### Environment Variables 
These are variables loaded into the codebase at runtime but not stored in the source code.  
**Setup**
1. Download `environs` package
```
python -m pip install environs[django]
```
2. Add the following lines to *settings.py*
```
from environs import Env
env = Env()
env.read_env()
```
3. Create a new file called `.env`, in the root directory. This has all the variables, add it to gitignore. 
4. In gitignore we could add all pycache folders, .pyc files, .DS_Store, etc.
5. Add db.sqlite3 file to gitignore as well
6. Set `DEBUG = False` in *settings.py*
7. Since we set debug as false, django assumes that we are pushing to production, so we need to update the ALLOWED_HOSTS list, this should look something like this `ALLOWED_HOSTS = [".herokuapp.com", "localhost", "127.0.0.1"]`
8. In the .env file, create a new variable with DEBUG=True, so here, the .env file stays in local and with local testing, the DEBUG is true but in prod the debug will be false.
9. Change `DEBUG = env.bool("DEBUG", default=False)` in *settings.py*. The default value would be false in case we have not found any environment variable.
10. Change `SECRET_KEY = env.str("SECRET_KEY")`. Secret key is a 50 character string generated at the start of a django project. This needs to be in .env file.
11. To generate a new SECRET-KEY - 
```
(.venv) > python -c "import secrets;
print(secrets.token_urlsafe())"
```
12. Update database in settings 
```
DATABASES = {
"default": env.dj_db_url("DATABASE_URL")
}
DATABASE_URL=sqlite:///db.sqlite3 # in .env file
```
13. To translate ORM into Postgres, install Psycopg
```
python -m pip install psycopg2
```
14. If we add a `.keep` file to an empty folder, git will track that folder.
15. Add `{% load static %}` at the top of base.html