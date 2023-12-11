# Docker

## Containerization
1. The way to setup codebases, tools, dependencies, etc and run project is different for different systems.
2. It helps define project configuration in a single file - Docker File
3. Helps running project in an isolated environment


## Docker Installation
1. Install docker
2. Run the following command to verify installation - `docker run hello-world`.
3. This should show "Hello from Docker!"
4. Check `docker` to check its cli.

## Docker
There are three main parts in docker
1. CLI
	1. The command line interface that allows us to run commands
	2. 
2. Engine
	1. The engine runs the commands.
	2. This helps us create images, run commands, etc.
	3. Called the docker-daemon
3. Registry (Docker Hub)
	1. To host docker images
	2. You can push your image to dockerhub and other services can pull this image from Docker Hub

### Images Vs Containers
Images are the templates from which containers are created.


### Dockerfile
Docker config is stored in a file called `Dockerfile`.  
This dockerfile describes how the image is supposed to run.  
1. The first line is `FROM <something>`. The `<something>` is called the `base image`. This base image represents from where we are building it.  
```
FROM node:20
WORKDIR <path>
COPY . .
RUN npm install
EXPOSE 3000
CMD ["node", "index.js"]
```
2. `WORKDIR` sets what is the working directory.
3. `COPY . .` everything from here to docker image, to the working directory.
4. `npm install` just installs external dependencies in package.json
5. `.dockerignore` is similar to gitignore. These wont be added to image.  
6. `EXPOSE 3000` just exposes that particular port.
7. `CMD` set of commands that need to be run when we are running the container. This runs when we are actually starting the container. 

**Build an Image** - `docker build . -t <image-name>`  
**List Images** - `docker images`  
**Run Image** - `docker run <image-name>` , alternatively `docker run -p 3000:3000 <image-name>` - this means that whatever request comes to machine 3000 port. forward to 3000 port of this image. We can use a `-d` flag which is detached mode, means that the terminal will not be hung with that container and we can run new commands in the same container.  
**Check current running status** - `docker ps`
**Stop container** - `docker stop <container-name>`. We can alternatively use `kill` to force stop a container.  
**Delete an image** - `docker rmi <image-name>`

### Push images to dockerhub
1. Signup in dockerhub
2. docker images are of the form username/imagename
3. login using `docker login`
4. To push, use `docker push <name>`
5. To pull, use `docker pull <name>`

Each step in dockerfile is a layer. During build each layer gets cached. If a layer gets uncached (changed), every layer after this needs to be re run and cached.  

## Volumes and Networks
1. We need volumes persist data. Once we shutdown a container and if there is any db in that container, all the data will be lost in restart.
2. We need networks so that one container can talk to another container. 


### Volume
A volume is a logical space where we can dump data from a container. If the container shuts down, the volume will remain the same until the volume is also shut down.  
**Create a volume** - `docker volume create <volume-name>` - this creates volume inside docker engine.  
**Delete a volume** - `docker volume rm <volume-name>`  
**Add volume to an image** - `docker run -v <volume_name>:<db folder> -p <port_a>:<port_b> mongo` - here , the db folder is the folder where data is dumped inside the container. This is different for different dbs.  
**List Volumes** - `docker volume ls`  
**SSH inside a container** - `docker exec -it <image-id> /bin/bash`  


### Networks
Since each container has its own network, we cant directly interact with another container through ports (since each container looks for the port within itself). This is where we use networks for communication between two containers.  
1. First create a network - `docker network create <network-name>`
2. List networks - `docker network ls`
3. When running a container, give it a name and attach it to a network - `docker run -p 3000:3000 --name <name> --network <network-name> <image-name>`
4. Now, we have a database and a backend container, in backend container we connect to db using the following code (mongo example) - `mongoose.connect("mongodb://localhost:27017/db, {});`. This needs to be replaced with `mongoose.connect("mongodb://<container-name>:27017/db, {});` if they are in the same network.  


## Environment Variables
These are config secret variables that need to be hidden while in production or anywhere else, eg - db urls, etc.  
We can add env variables by - `docker run -p 800:800 -e <var-name>=<value> <img-name>`. 

## Multi Stage Builds
The file running will be different in dev and prod (eg - debug true and false, etc). 
```
FROM node:20 AS base
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install

FROM base AS development
COPY . .
CMD ["npm", "run", "dev"]

FROM base AS production
COPY . .
RUN npm prune --production
CMD ["npm", "run", "start"]
```
Here, line 1-4 builds the image as base. The dev and prod are run as per the base image.  
To run dev, use - `docker build . --target development -t app:dev`, run with `docker run app:dev`

## Docker Compose
It lets us compose a bunch of images together. Through compose, we use a single YAML file to describe all the applications services. So, with a single command, all the services will be run.	
```
services:
  mongodbi_db:
    image: mongo:latest
    ports:
      - "27017:27017"
    volumes:
      - mongodb-data:/data/db
  custom_app:
    build: ./
    ports:
      - "3000:3000"

volumes:
  mongodb-data:
 ```
The file name would be `docker-compose.yaml`  
To run this, run `docker-compose up`  
When we use docker-compose, all the services inside it are already connected by a network