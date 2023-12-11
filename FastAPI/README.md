# FastAPI

## Intro
1. We need to setup our virtual environment, add version control.
2. Install *fastapi* package - `pip install fastapi[all]` -  we can omit the \[all\], but this adds all the other dependencies too.
3. Generate `requirements.txt`

## First App
```
from fastapi import FastAPI

app = FastAPI() # FastAPI instance


@app.get("/") # get method with path
async def root(): # async function
    return {"message": "Hello World"} # data to return from get method
```
**Run the app** - `uvicorn <filename>:<fastapi_instance> --reload`  
1. Uvicorn is installed in \[all\] so we dont need to use this seperately.  
2. The reload flag tells the server to restart after every code change.  
3. In FastAPI, for a given path, if it finds two functions with same path, it runs only the first matched function.   
4. We use Postman to test the post, put, patch methods

### Post Request
```
@app.post("/createpost")
async def create_post(payload: dict = Body(...)): 
    return {
        "message": "Post Succesfully Created"
    }
```
1. `payload: dict = Body(...)` takes all the parameters from payload body, convert it into a dict, store it in a variable for payload.  
2. We need to have a schema for the data to be sent, along with some rules for the data. We will use **Pydantic** for this.

### Pydantic
1. Pydantic is a part in fastapi\[all\]. 
2. We can create schemas using Pydnatic
```
from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    <var>: <dtype> = <default-value >
    content: str
    published: bool = True
    rating: Optional[int] = None
```
4. Then we can use this variable to enforce type in post requests.
```
async def create_post(post: Post):
```
5. `<pydantic_model_instance>.model_dump()` - converts pydantic model to dictionary.
6. `@app.get("/posts/{id}") async def get_posts(id: int):`, Here the `{id}` is called the path parameter, this is automatically passed into the function through that variable. We use type hinting to assert that datatype for validation. 
7. We can add a response object to the function to updates its repsonse status - 
```
get_posts(id: int, response: Response):
response.status_code = status.HTTP_404_NOT_FOUND 
```
Alteratively we can use another method - `raise HTTPException(status.HTTP_404_NOT_FOUND, detail = "Post Not Found")`   
8. To add a status code to the method itself, use - `@app.post("/posts", status_code = status.HTTP_201_CREATED)`

### Delete
```
@app.delete("/posts/{id}", status_code = status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):

    for ind, post in enumerate(posts_array):
        if post['id']==id: 
            posts_array.pop(ind)
            return Response(status_code = status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Post does not exist")
```

### Update
```
@app.put("/posts/{id}")
async def update_post(id: int, updated_post: Post):
    post_new = updated_post.model_dump()
    for ind, post in enumerate(posts_array):
        if post["id"] == id:
            post_new['id'] = id
            posts_array[ind] = post_new
            return {
                "message": "Post Updated"
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Post Not Found")
```

*FastAPI has inbuilt documentation support, just go to `base_url/docs` to get all the documentaion of API through Swagger, if you use `base_url/redoc` then you will get the documentation from Redoc*  

### Folder Structure
```
project/
├── app/
│   ├── main.py
│   └── others
├── models/
│   └── model
├── venv
├── requirements.txt
└── gitignore
```

## Databases
1. We will use postgres for this. Postgres is an SQL db. After installing postgres, this creates a default db with name `postgres`.
2. We use `SQLAlchemy` as the ORM.

### SQLALchemy
1. `pip install sqlalchemy`
2. SQLAlchemy needs a db driver for the db that we use - postgres, mysql, etc. We need to have this driver seperately. For postgres, we have `psycopg2`. This is already installed from fastapi-all.
3. We can create a folder for models, and name it *database/* inside have files for *connection.py* and *model.py*.
4. Basic Code - *connection*
```
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:raghu@personal_server/fastapi_db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@serve_name/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```
5. Basic Code - *model* 
```
from .connect import Base
from sqlalchemy import Boolean, Column, Integer, String

class Post(Base):
    __tablename__ = "posts" # table name in postgres

    id = Column(Integer, primary_key = True, nullable = False)
    title = Column(String, nullable = False)
    content = Column(String, nullable = False)
    published = Column(Boolean, nullable = True)
```
6. Basic Code - *In App*
```
from database import model
from database import connect

app = FastAPI()

# to bind db engine to app
model.Base.metadata.create_all(bind = connect.engine) 

# Add Dependency, we get a connection/session to our database
def get_db():
    db = connect.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/databasetest")
async def test_db(db: Session = Depends(get_db)): # this session should be a part of every route
    return {
        "message": "Database Connect Succesful"
    }
```
7. SQLAlchemy doesnt help in migrations, so we use `Alembic`. 
8. Get all data from table - `posts = db.query(model.Post).all()`
9. Post data into the table -
```
@app.post("/posts", status_code = status.HTTP_201_CREATED)
async def create_post(post: Post , db: Session = Depends(get_db)):

    new_post = model.Post(
        title = post.title, 
        id = post.id, 
        content = post.content,
        published = post.published
        )
    # alternatively use
    # new_post = model.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return {
        "message": "Post Succesfully Created",
        "data": new_post
    }

```
10. We use the pydantic model for data validation
11. `.all()` - gets all the data matching, `.first()` - gets only the first column matching, useful for primary key searches.
12. Query over data - `post = db.query(model.Post).filter(model.Post.id == id).first()`
13. Delete request has no response - 
```
post.delete(synchronize_session=False)
db.commit()
```
14. Update post - 
```
post_query.update(
        post.model_dump(),
        synchronize_session=False
    )

    db.commit()
```
15. We use pydantic models for structuring requests and responses. When we pass a request, pydantic checks and makes sure that all the data and attributes are there accordingly. 
16. We can use pydantic models for both gettings requests, and as well as sending responses. We can use class inheritance for cleaner code.
17. We can create seperate file for storing pydantic models, here we will specify the request and response models. eg - 
```
# Pydantic Model for Response
class Post(BaseModel):
    id: int
    title: str
    content: str
    #published: bool = True

    class Config:
        orm_mode = True #this here is helpful in generating other fields, for eg - in pyndatic we could have only few items and not all items present in DB model, but this mode will help us in convering it to DB model

# POST Function
@app.post("/posts", status_code = status.HTTP_201_CREATED, response_model = Post)

# Get list of posts
@app.get("/posts", response_model = List[Post])
```

### Relationships
1. We use foreign keys for joins and relationships, we need to setup FKs using SQLAlchemy.
2. Code - `owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))`
3. We can add `owner = relationship("User")` this way, based off on relationship, it will get the User object accordingly. This can further be used in Pydantic Models

### Joins in SQLAlchemy
```
result = db.query(Post, func.count(Vote.post_id).label("votes")).join(Vote, Vote.post_id==Post.id, isouter = True).group_by(Post.id).all()
```

### Query Params
1. We can setup differnet query params. We an pass them as args in the func signature and query accordingly.
2. We can set limits, offsets, etc.
```
def foo(limit: int=10, skip:int = 0, search:Optional[str] = "")
```
### CORS
1. CORS stands for Cross origin resource sharing
2. It allows you to make requests from web browser in one domain to server in another domain. 
3. By default our API does not allow it.
```
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # allow all http methods
    allow_headers=["*"], # allow all http headers
)
```

### Migrations
1. SQLAlchemy cannot update database if we make any changes to the class, so we need a database migration tool
2. We use the library `alembic`
3. Install Alembic - `pip install alembic` 
4. We can see alembic commands through - `alembic help`
5. We need to start alembic so use `alembic init <foldername>` This creates a folder for alembic with the name we give
6. Alembic creates a folder with the given name and we have the following files inside it - env.py, README, script.py.mako. env file is the most important file there.
7. There needs to be some setup in env file. 
8. It needs to have access to the `Base` variable, so import it in env file. This gives access to all the SQLAlchemy models. We import it from model file and not connect file, because all the subclasses are in the model file, so to get access to them, we need to import it from model file.
9. Update the target_metadata variable - `target_metadata = Base.metadata`
10. Next we need to add the path of databse in the alembic.ini file, but hardcoding this is not a good idea, so the approach is to override this in the env.py file by setting up a config variable
```
# env.py file
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
```
11. The setup is done
12. When we want to make a change to our database, we create a revision, revision is what tracks those changes. 
13. To create a revision - `alembic revision -m "First Revision"`
14. This creates a file under versions folder. The file has two functions - revision_number, upgrade and downgrade, here we make all the changes. Looking at alembic documentation is very helpful here. 
15. We can run `alembic upgrade <revision_num> or +1|+2..` to run a particular upgrade.
16. Alembic also creates a table in db called `alembic_version` this just has the list of revisions in a single column.
17. Flow: Create Revision -> Write upgrade and downgrade -> run upgrade
18. Ex - Upgrade: Create Column, Downgrade: Delete Column
```
op.add_column(<tablename>, sa.Column('name', <dtype>, nullable=))
```
19. `alembic upgrade head` will update to the latest revision since head variable has the latest rev 
20. `alembic downgrade <down_revision>/ -1|-2|..` - to rollback
21. `alembic history` -  commit log
22. `alembic --autogenerate -m "message"` - generates table based on Base
23. Now, we can add cols in model, then run autogenerate to make sure its done.
24. We can remove base statement in app for creating table since its done with alembic now.

## Users & Authentication
1. We create user model and table, like posts.
2. To hash passwords we use `passlib` and the algorithm used is `bcrypt`, so use - `pip install passlib[bcrypt]`
3. The code would be
```
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
user.password = pwd_context.hash(user.password)
```
4. We can create `utils.py` file for writing util functions
5. `from .` - same folder, `from ..` - a folder above

### Routers

1. Routers are used to group a bunch of requests, create a folder named `routers` and create different files for different bunch of routes
2. Now, these routers need to have the `app` for routing, the workaround is, in each router file add the following code -
```
from fastapi import APIRouter
router = APIRouter(
    prefix = "/users" # here all requests will start with this string and we can remove that string from all routes in the file.
    tags = ['Posts'] # this will group all this router requests into a single group in the docs
)

#replace all @app with @router
```
4. In main file with app variable, add the following code - 
```
app.include_router(post.router)
app.include_router(user.router)
```
5. Now, the flow of control starts with the app, then goes to each router, checks the path and returns.

### Authentication
1. We have two methods of authentication, one is session another is JWT. In session, we store data in our server that a particular user is authenicated.
2. In JWT, once the user sends correct email and password, we generate a JWT token and sent it back to the user, this token is sent by user when it calls other requests, so we know the user is authorised and authenticated.

#### Anatomy of a JWT token
A JWT token has three components -   
1. Header - This contains the encryption algo and the type of algo.
2. Payload - This can be anything we define, which helps us identify user, we keep it as minimal as possible
3. Signature - This is a combination of `header + payload + secret`. This secret is only pertaning to our server and this should never be revealed. 
4. These three components make up a JWT token.

#### Authentication Steps
1. We authenticate usually, comparing passwords. Helpful functions
```
return pwd_context.hash(password)
return pwd_context.verify(plain_password, hashed_password)
```
2. Now, we have checked the validity of the user, now we need to create a JWT for the user. 
3. To create JWT, install - `pip install python-jose[cryptography]`
4. Here is a method to create JWTs
```
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "VOIDVOIBsvviwpichpcVPDVPpvppd[rk[mvwpovwnpincd]]"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):

    # create a copy of data
    data_to_encode = data.copy()

    # set expire time
    expire_time = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data_to_encode.update({
        "exp": expire_time # here "exp" is claimed name, if we dont use this, datetime will not be serialized in JSON
    })

    print(data_to_encode)

    jwt_token = jwt.encode(
        data_to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return jwt_token
```
5. The data we pass can be very minimal, it could just be the user_id.
6. Instead of using pydantic user model in login request, we could use fastapi oauth2 request - `credentials: OAuth2PasswordRequestForm = Depends()`
7. Here, the fields are username and password, and it is in form-data, not in body.
8. Code for token verification
```
oaut2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_token(token: str, credentials_exception):
    
    try:
        decoded_token = jwt.decode(token, 
                                   SECRET_KEY, 
                                   algorithms=[ALGORITHM])
        user_id: str = decoded_token.get("user_id")
        if not user_id:
            raise credentials_exception
        
        token_data = Token(id = id)
        return token_data
    
    except JWTError:
        raise credentials_exception
    
def validate_user(token: str = Depends(oaut2_scheme)):
    credentials_exception = HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                                          detail="Could not find token",
                                          headers={"WWW_Authenticate": "Bearer"})
    
    return verify_token(token, credentials_exception)
```
9. Here, the validate_user function is used to fetch token from the url, since its dependent on oauth2scheme and that scheme is linked to login url, the token is automatically fetched and checked. We can now add this valid_user as a depedency to check if the user is logged in or not.
10. Now, add this - `user_id: int = Depends(validate_user)` can be added to any function signature to force log in from user.


## Environment Variables
1. We need to setup variables in our code based on the environment we are in (dev, prod)
2. When we read an env variable, it is always gonna come up as a string. To get ints, etc, we use pydantic for the validation and typecasting.
3. The procedure here is - 
4. Create a file called `config.py`
5. Create a class called Settings, and describe all the variables inside it, with datatypes and create an object for it. This object will be imported throughout.
```
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    SECRET_KEY: str
    ALGORITHM: str
    TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env" # env file path

settigs = Settings()
```
6. Create a `.env` file and add all the variables, add it to gitignore.
```
ALGORITHM=HS256
TOKEN_EXPIRE_MINUTES=30
```


## Docker
1. Use Python Image as the base image

## Testing
1. We use `pytest` for  - `pip install pytest`
2. To run testing we use - `pytest`
3. Pytest has a auto discovery feature where it looks at all the files and looks for test
4. It looks for test_*.py files or *_test.py files.
5. Add init file to make a package called tests and add testfiles in it.
6. The output has '.'s which represent the number of tests created, green dot is passed test, red dot is failed test.
7. We can run those files with pytest as well
8. The functions should also start with test*.py files
9. `pytest -v` gives us the list of tests and their status
10. we pass `-s` flag to print statements in testing functions
11. We use assert statements to verify result and function
```
import pytest
@pytest.mark.parametrize("num1, num2, expected", [
    (7, 3, 10),
    (4, 3, 7)
])
def test_add(num1, num2, expected):
    assert num1+num2 == expected
```
12. We can use fixtures - it is a function that runs before each one of your tests
```
import pytest

@pytest.fixture
def fixture_example():
    return 1

def test_fixtures(fixture_example):
    assert fixture_example == 1
```
13. We use this for things like setting up bank database, etc.
14. Anytime we throw an error, the test automatically fail
```
def test_fixture2(fixture_example):
    # testing exceptions
    with pytest.raises(Exception): # this tells pytest to look for an exception
        # if this raises an exception, then the test passes
        # if an exception is not raised, then the test fails
        # the exception can be anything, but it must be an exception
        # the exception we pass, should be the same exception that should be raised
        assert fixture_example == 0
```
15. FastAPI provides a testclient for us. This object is used to make requests to our API, what we can do with requests library, we can do with this client.
```
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    res = client.get("/") # this gives a response object
    assert res.json() == {"message": "Hello World"}
    assert res.status_code == 404
```
16. We can use --disable-warnings flag to disable warnings
17. We can use `pytest -k <keyword>` to run tests with a particular keyword
18. We can pass `-x`flag to stop testing after first failure    
19. We can setup test database and test client in conftest.py file, this file is automatically imported by pytest
20. We can use `@pytest.fixture(scope="module")` to run the fixture only once per module
21. To setup the testdb, We copy all the connect logic and create new objects for session, get_db etc. Here we need to setup an override such that, when the test function calls the real get_db function, it should call the overriden_test_db function instead. This dependency override is done using - `app.dependency_overrides[get_db] = override_get_db`
22. We create a new db called test_db in postgres and create all tables in it.
23. We can have fixtures that depend on other fixtures, just pass the fixutre name as an argument to the function
24. `/users` will get redirect to `/users/` so we need to add a `/` at the end of the url, the code would be 3xx status code
25. We can use `pytest --cov=app` to get the coverage of the app
26. We can use `pytest --cov=app --cov-report=html` to get the coverage in html format
27. To set test data in form-data, instead of using `json=` we use `data=` and pass a dictionary
28. Fixtures by default have a scope of function, so they run before every test, we can change this by passing `scope="module"` to the fixture
29. We can use `@pytest.mark.skip` to skip a test
30. We define all the fixtures in conftest.py file, this file is automatically imported by pytest and it is accessible to all the tests.
31. confest.py file is only scoped at folder level.
32. We use fixtures to setup test data, test client (both authorized and unauthorized), test db, etc.

## CI/CD
1. Continuous Integration - Automated way to build, test and package applications .
2. Continous Delivery - Picks up where CI ends and automates the delivery of packages.
3. CI/CD tool provides a runner (VM) to run our code. These commands are configured in a file called `.gitlab-ci.yml` and it can be an yaml or json file.
4. These commands make up the actions that the pipeline will perform. This pipeline will be triggered off some event (code pushes)
5. We can use `gitlab-runner` to run the pipeline locally.

### Setting up Github actions
1. In the repo, create a folder called `.github` and create a folder inside it called `workflows`. Inside this create a file called `main.yml`
```
name: Build and deploy code
# when to run the workflow
# happens on every single pull and push on every branch
on:
  # provides a list of branches to run the workflow on for each action
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
# once we provide a trigger, we need to provide a job
jobs:
  job1:
    # provide the type of machine to run the job on
    runs-on: ubuntu-latest
    # define the list of steps to run, 'uses' is the action to run and 'run' is the command to run
    steps:
      - name: pulling the git repo into the machine
        uses: actions/checkout@v2
      - name: setting up python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: update pip
        run: python -m pip install --upgrade pip
      - name: installing dependencies
        run: pip install -r requirements.txt
      - name: running tests
        run: pytest
```
2. This is the example of a workflow, we can add more jobs to it, we can add more steps to it, we can add more triggers to it.
3. We need to add env variables to it for it to run properly, so for that we need to use github secrets
4. We can go to repo -> settings -> secrets -> actions secrets -> new repository secret -> add the key value pair
5. We can use these secrets in the workflow file using `${{ secrets.<key> }}`
6. We can also create environments for dev, prod, etc and add secrets to them.
7. Then we can add that environment to the job in the workflow file using `env: <env-name>`