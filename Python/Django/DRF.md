# Django REST Framework

## Setup
Setup is similar to how we setup a django project. We create a venv, create gitignore file, start a django project.  
Install DRF along with django in the venv. To install DRF, use
```
python -m pip install djangorestframework
```

## Web APIs

### Internet Protocols
1. First, when we hit a url, the url goes to the DNS (after searching through local cache and ISP cache), and then we get the IP address for the server. 
2. Then, we set up a consistent connection with the server through TCP, using a three way handshake. The three way handshake works in the following way -
   1. The client sends an `SYN` asking for a connection
   2. The server responds with a `SYN-ACK` that acknowledges the request and passes a connection parameter
   3. The client sends an `ACK` back to server acknowledging the connection.

### HTTP

**HTTP Protocols**
1. **POST** - To create new resource
2. **GET** - To fetch a resource
3. **PUT** - To update an existing resource
4. **DELETE** - To remove a resource

In an API, we have several endpoints and each point returns particular data in a json/xml format.  
When an endpoint returns multiple data resources, we call it a **collection**.  
HTTP is a request response protocol between two computers that have an existing TCP connection.  
Each HTTP message contains -
1. Status line - This is a request line or response line, containing data about the request status
2. Headers - Each respone/request has a set of headers, like metadata for the response
3. Optional Body Data - If there is any response data 

**Status Codes**
1. 2xx - Success
2. 3xx - Redirect
3. 4xx - Client side errors
4. 5xx - Server side errors

HTTP is a stateless protocol. It means that each request/response is independant of another. There is no memory of past interactions.

### REST API
Principles of REST API - 
1. Stateless - Like HTTP
2. Uniform Interface
3. Client - Server Decoupling
4. Cacheablity
5. Layered System Architecture
6. Code on Demand (Optional)

## Django-REST-Framework
DRF works alongside with Django. We cannot create an API simply with DRF. We need to setup and configure django, and then start with DRF. 

**Checklist**
1. Create a virtual environment
2. Add all to *.gitignore*
3. Install Django, DRF.
4. Start a Django project.
5. Migrate everything.
6. Intialise git
7. Check if everything is working fine by running the server

**Checklist for App**
1. Create a new App
2. Add the app to settings.py
3. Create a new model, makemigrations for it, register the model in admin
4. Create superuser
5. Create a listview
6. Setup project level url for the app
7. Create urls.py in app, add the url for the view
8. Create templates folder and update settings.py
9. Create a template for a view
10. Write Tests

### DRF Setup
1. Install the package with pip.  
2. Add DRF to *settings.py* - `"rest_framework",`.
3. We need to create a new app called `apis`. This will have all the functionality for the API.
4. Create the `api` app and add it to *settings.py*.
5. In the project level urls, add a new url for apis. This url should typically start with `"api/"`.
6. Create a new `urls.py` file for apis and add a url for list.
7. Create a new view for this api list.

DRF relies on model, url, and a file called serializer to send the responses. Let us look at our view - 
```
from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer

class BookAPIView(generics.ListAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
```
Here we created a ListAPIView, similar to ListView in Django, but for APIs. We got this from the generics class of Django. We create a new API view, we define a queryset, and a serialiser class which we need to define. 

### Serializers
A serializer converts complex modelsets and querysets into an easily consumable format, typically a JSON file. Let us look at an example serialiser.  
Create a `serializers.py` file in the app.
```
from rest_framework import serializers
from books.models import Book
class BookSerializer(serializers.ModelSerializer):
   class Meta:
      model = Book
      fields = ("title", "subtitle", "author", "isbn")
```
We create a serializer class, adda a model and the fields we need to serialize.  
So, in DRF, the way goes from URL -> View (Fetch Data) -> Serializer (JSON the data) -> User  
Go to the `api/` endpoint after running server to see how the data is rendered.  

### Testing
Testing Django APIs is similar to testing Django Apps, there are predefined classes to help us test the instances.  
```
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book
class APITests(APITestCase):
   @classmethod
   def setUpTestData(cls):
      cls.book = Book.objects.create(
      title="Django for APIs",
      subtitle="Build web APIs with Python and Django",
      author="William S. Vincent",
      isbn="9781735467221",
      )
   def test_api_listview(self):
      response = self.client.get(reverse("book_list"))
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(Book.objects.count(), 1)
      self.assertContains(response, self.book)
```
### Extras
DRF specific settings all exist under a configuration called `REST_FRAMEWORK`. This can be added at the bottom of the *settings.py* file. Add the following -
```
REST_FRAMEWORK = {
   "DEFAULT_PERMISSION_CLASSES": [
      "rest_framework.permissions.AllowAny",
   ],
}
```
This allows unrestricted access whether a request is authenticated or not. 

### CORS
CORS stands for cross-origin-resource-sharing. This refers to the face that whenever whenever client interacts with API hosted on different domains, there are particular security vulnerabilities.  
CORS requires web server to include specific HTTP headers that allow the client to determine if and when cross domain requests should be allowed.  
The easiest way to handle this is to use middleware that will automatically include the headers as per the settings. The package to be used is `django-cors-headers`.
```
python -m pip install django-cors-headers
```
Next - 
1. add `corsheaders` to INSTALLED_APPS
2. add CORSMIDDLEWARE above COMMONMIDDLEWARE in MIDDLEWARE
3. create a `CORS_ALLOWED_ORIGINS` config at the bottom of the file.
```
INSTALLED_APPS = [
   "corsheaders", 
]
MIDDLEWARE = [
   ....,
   "corsheaders.middleware.CorsMiddleware",
   # new
   "django.middleware.common.CommonMiddleware",
   ....
]
CORS_ALLOWED_ORIGINS = (
   "http://localhost:3000",
   "http://localhost:8000",
)
```

### CSRF
Django provides CSRF protection for forms, but this is not always the case for frontend frameworks. We need to whitelist the ports from which form requests come. The default port for React is 3000. We need to whtielist it by adding the following line at the end of the settings.py file. 
```
CSRF_TRUSTED_ORIGINS = ["localhost:3000"]
```

## Permissions
DRF comes with several permissions that we can use to secure our web application. They are divided into 3 types - 
1. Project Level
2. View Level
3. Model Level

### Project Level Permissions
Project level permissions are configured in a single variable called `REST_FRAMEWORK`. There are 4 types
1. AllowAny - any user, authenticated or not, has full access
2. IsAuthenticated - Only authenticated users have access
3. IsAdminUser - Only admin has access
4. IsAuthorizedOrReadOnly - unauthorized users have access to read, authorized users can write, update, delete.
For any 4 of these to be implemented, the `DEFAULT_PERMISSION_CLASSES` setting need to be updated.

### Log In and Log Out
We can directly let the user login with rest_framework. Add the following to project level urls -
```
urlpatterns = [
   ...
   path("api-auth/", include("rest_framework.urls")),
]
```
This setup allows login in the Browsable API page.

### View Level Permissions
We can setup permissions to view level, so as to give fine grain control access over the api. We can do this with the help of `permission_classes`.  
We can add `permission_classes = (permissions.IsAdminUser,)` to a particular view. Only admin will have access to that view.

### Custom Permissions
DRF relies on the `BasePermission` class. All other permission classes are inherited from it. It has two functions - 
1. has_permission(self, request, view)
2. has_object_permission(self, request, view, object)

For a custom permission class, we can override both these methods.  
Create a new *permissions.py* file and add check the following permissions.
```
class IsAuthorOrReadOnly(permissions.BasePermission):
   def has_permission(self, request, view):
      # Authenticated users only can see list view
      if request.user.is_authenticated:
         return True
      return False
   def has_object_permission(self, request, view, obj):
      # Read permissions are allowed to any request so we'll always
      # allow GET, HEAD, or OPTIONS requests
      if request.method in permissions.SAFE_METHODS:
         return True
      # Write permissions are only allowed to the author of a post
      return obj.author == request.user
```
We can add this class in the `permission_classes` variable, instead of the earlier default permission

## User Authentication
User Authentication is the process of verifying an actual user. Based on this, the user can login, logout, register, etc.  
Django uses cookies for tracking users, but since HTTP is a stateless protocol, we need to pass a unique identifier. There are 4 different built-in authentication options in django. 
1. Basic
2. Session
3. Token
4. Default

### Basic Authentication
When a client makes an HTTP request, it is forced to send an approved authentication credential before access is granted.  
**Steps**
1. Client makes a request
2. Server responds with a 401 error and `WW-Authenticate` header that tells us how to authorize
3. Client sends back the credentials via the Authorization HTTP header
4. Server checks credentials and sends a 2xx or 4xx response.
Once approved, the client sends all future requests with this authorization HTTP header.   
The credentials sent are unencrypted base64 encoded.   
The major advantage is its simplicity, but every single request needs to be verified against all existing user credentials to check if its correct or not. It is also not encrypted so it is insecure. This should only be used via the HTTPS protocol.

### Session Authentication
The client authenticates with its username and password, and the server sends back a sessionID. This id is then passed in the header of all requests.  
The server can look up this session id to get a session object. This contains all the details of the user.  
**Steps** 
1. User sends credentials
2. Server verifies them and sends a session id or 4xx error if incorrect
3. Server creates a session object and sends the id, which is stored as a cookie in the browser
4. All requests are sent with this ID as header, and server verifies and the requests proceed
5. After log out, the session object is destroyed, both by client and server

Default setting in django is a mixture of basic and session authentication. The session id is generated, and this ID is passed through the header via the 

### Token Authentication
This is similar to session, but here only a token is generated and session object is created. Here, each time the token is sent to server, the server just checks if the token is valid. 
Once the user verfies credentials, the server sends a token id and that token is stored in the clients cookies.  
Django uses `TokenAuthentication` to internally implement token auth.  
JWT (JSON Web Token) is a new form of token contains cryptographically signed tokens. They were originally used in `OAuth`. 

### Default Authentication
Just like `DEFAULT_PERMISSON_CLASSES`, we have `DEFAULT_AUTHENTICATION_CLASSES`.
```
REST_FRAMEWORK = {
   "DEFAULT_PERMISSION_CLASSES": [
      "rest_framework.permissions.IsAuthenticated",
   ],
   "DEFAULT_AUTHENTICATION_CLASSES": [
      "rest_framework.authentication.SessionAuthentication",
      "rest_framework.authentication.BasicAuthentication",
      "rest_framework.authentication.TokenAuthentication",
   ],
}
```
For token authentication, we need to add the `authtoken` app which generates the token. It comes with drf, but needs to be added to INSTALLED_APPS manually - `"rest_framework.authtoken",`.   
Since we updated the INSTALLED_APPS, we need to migrate.  
Now that we added authentication, we need to add urls for login and logout. We use two packages for this - `dj-rest-auth` and `django-allauth`.  
`dj-rest-auth` comes with login, logout, passwordreset functionality.  
**Setup**  
1. Download dj rest auth - `python -m pip install dj-rest-auth`. 
2. Add it to INSTALLED APPS -  `"dj_rest_auth",`
3. Add it to project level urls - `path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),`
4. The endpoints for login, logout and password reset are predefined.  

### Registration
This is done with `django-allauth`. This package comes with diffent features like authentication with social media as well.
1. Install the package - `python -m pip install django-allauth`
2. Add the following configs to INSTALLED_APPS in django - 
```
"allauth",
"allauth.account",
"allauth.socialaccount",
"dj_rest_auth",
"dj_rest_auth.registration",
```
3. Add allauth to templates. templates -> options -> context_processors - `"django.template.context_processors.request",`
4. Add email backend - `EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"`. This config is used to send emails.
5. Add site id - `SITE_ID = 1`. This is used to host multiple websites from the same project.
6. Add it to middleware - `'allauth.account.middleware.AccountMiddleware'`

We can also setup user registration - 
1. Add url for registration - `path("api/v1/dj-rest-auth/registration/",include("dj_rest_auth.registration.urls")),`


## Viewsets and Routers
1. **Viewsets** - It can replace multiple related views
2. **Routers** - It automatically generates URLs for the developer.

Instead of multiple views which perform the same action, we can use ViewSets.
```
class PostViewSet(viewsets.ModelViewSet):
   permission_classes = (IsAuthorOrReadOnly,)
   queryset = Post.objects.all()
   serializer_class = PostSerializer
class UserViewSet(viewsets.ModelViewSet):
   queryset = get_user_model().objects.all()
   serializer_class = UserSerializer
```

Routers use viewsets to generate automatic URLs for us. 
```
router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", PostViewSet, basename="posts")
urlpatterns = router.urls
```

## Schema & Documentation
A schema outlines all avaiable end points, a documentation tells us how to use those endpoints. We use `drf-spectacular` to generate schema. 
### Setup
1. Install it - `python -m pip install drf-spectacular`
2. Add it to installed apps - `"drf_spectacular",`
3. Register it within the REST_FRAMEWORK config in settings.py - `"DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",`
4. Add metada about schema in settings.py - 
```
SPECTACULAR_SETTINGS = {
   "TITLE": "Blog API Project",
   "DESCRIPTION": "A sample blog to learn about DRF",
   "VERSION": "1.0.0",
   # OTHER SETTINGS
}
```
5. To generate a schema file, we use the following command - `python manage.py spectacular --file schema.yml`
6. To generate schema dynamically, create a new url in project level urls and use the following route - 
```
from drf_spectacular.views import SpectacularAPIView
urlpatterns = [
   ...
   path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
   ...
]
```
If we hit this url, we generate a new schema for the api. 

There are two tools that work with drf_spectacular - `Redoc` and `SwaggerUI`. To do this, add the following code in project level urls.py - 
```
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularSwaggerView
urlpatterns = [
   ...
   path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc",),
   path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
   ...
]
```

Deployment is similar to how we do it with django. The environment variable setup, and everything.

