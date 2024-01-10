# Jenkins

**Resource** - https://www.youtube.com/watch?v=6YZvp2GwT0A&ab_channel=DevOpsJourney

## Intro
1. It is an automation platform that allows us to build, test and deploy our software through pipelines.
2. It has a master-slave architecture. The Master server is responsible for managing the jobs, dispatching build jobs to slaves for the actual execution. It schedules builds and controls the pipelines
3. The slaves are called minions. They are responsible for the build jobs execution. They are disposable and can be created and destroyed on demand.
4. Eg - A user commits to a git repo, the master server detects the change, pulls the code and dispatches the build job to a minion. The minion executes the build job and reports the result back to the master server.
5. Agent Types:
    1. Permanent agents - These are dedicated servers for running jobs. They need to have java and ssh setup. The build tools we need are also installed. They are always connected to the master server. They are used for long running jobs.
    2. Cloud agents - They are created on demand and destroyed after the job is done. They are used for short running jobs. Eg - Docker containers, AWS EC2 instances, etc.
6. Build Types:
    1. Freestyle - It is a simple build job. It is a sequence of build steps. It is used for simple build jobs.
    2. Pipeline - It is a collection of build steps that can be executed in sequence or in parallel. It is used for complex build jobs. The files are written in groovy. These are broken into different stages.
7. Setup - https://github.com/devopsjourney1/jenkins-101
8. Do not put spaces in the job name. It will be replaced by %20 in the url.