# Jenkins

**Resource** - https://www.youtube.com/watch?v=6YZvp2GwT0A&ab_channel=DevOpsJourney

## Intro
1. It is an automation platform that allows us to build, test and deploy our software through pipelines.
2. It has a master-slave architecture. The Master server is responsible for managing the jobs, dispatching build jobs to slaves for the actual execution. It schedules builds and controls the pipelines
3. The slaves are called minions. They are responsible for the build jobs execution. They are disposable and can be created and destroyed on demand.
4. Eg - A user commits to a git repo, the master server detects the change, pulls the code and dispatches the build job to a minion. The minion executes the build job and reports the result back to the master server.
5. Agent Types:
    1. Permanent agents - These are dedicated servers for running jobs. They need to have java and ssh setup. The build tools we need are also installed. They are always connected to the master server. They are used for long running jobs.
    2. Cloud agents - They are created on demand and destroyed after the job is done. They are used for short running jobs. Eg - Docker containers, AWS Fleet Managers, etc.
6. Build Types:
    1. Freestyle - It is a simple build job. It is a sequence of build steps. It is used for simple build jobs.
    2. Pipeline - It is a collection of build steps that can be executed in sequence or in parallel. It is used for complex build jobs. The files are written in groovy. These are broken into different stages.
7. Setup - https://github.com/devopsjourney1/jenkins-101
8. Use this URL to setup jenkins using docker - https://www.jenkins.io/doc/book/installing/docker/
9. Do not put spaces in the job name. It will be replaced by %20 in the url. Each job has a folder created for it
10. We can run a simple job with freestyle job, we can run a bash script like
```
echo "The build url is ${BUILD_URL}"
```
11. Here, the build_url is an env variable for jenkins and we can print them in bash using `${}`
12. We can go into the jenkins folder structure, to ssh into docker container, use `docker exec -t <docker-jenkins-container-name> bash`
13. Go to `var/jenkins_home/workspace` to see all the jobs

## Pipelines
1. We write pipelines in groovy syntax, we can write the pipeline in the UI, or create a `Jenkinsfile`. We can put whatever filename for jenkinsfile, but the same name should be in script path in the pipeline script from scm
```
pipeline {
    agent { 
        node {
            label 'jenkins-agent-goes-here'
            }
      }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                echo "doing build stuff.."
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                echo "doing test stuff..
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
```
