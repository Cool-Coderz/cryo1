# Docker and how to use it.


## What is docker?:
Docker is what is called a containerization software.  basically it uses what it can from your host machine or vm and applies what it doesn't have as really git commits.  sort of like if you were building a simple 4 block structure and you already have the first block... but you need the rest.


## what is docker used for?:
Docker is great for working against throw away development builds.  meaning you might git pull a new Dockerfile that holds an updated version of what someone did.  and after you rebuild and run the docker file.. you will be up and running with the new changes.  when you are done.. you can simply stop the container, remove the container and remove the image if you wish.  this stuff will never touch your host OS, except to work off of what is already in your kernel.


## Builds:

### We will use one basic set of instructions for now for our builds.  hopefully we can get everyone to get to the same place faster this way.
1) install virtualbox for your OS
2) download ubuntu 18.04 (desktop is more comfortable for most)
3) create a virtual machine within virtualbox using the ubuntu 18.04 file.  you should only need maybe 1 Gbs of ram and 1 core for now.  If you can do dynamic disk... do it..  if you can't... set aside maybe 20GBs of disk space for the virtual machine.
4) install docker: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04

if all goes well you can move down to the next section.



## how to work with docker:
1) navigate to your local copy of https://github.com/Cool-Coderz/cryo1/build/docker/images/base_image
2) run the download_files.sh file only once.  this will download the centos7 epel-release.. which is some irritating update that it needs.
 - run the file like this: "$ ./download_files.sh"
3) once those are done... you can simply run the next script: "$ ./rebuild_image.sh" .  this initial build will take probably a good 15 minutes to run.
4) check to see if the image has been built: "$ docker image ls"

So, now you will be stuck with an image that you can't use at the moment... but if you got to this point... your doing great.  remember this is just the main building block for any changes we make later on.  you should never need to do this part again, unless we change to a different version of some package or OS at this level.


## Docker terminology and descriptions:

Descriptions:
 - a docker file by default has to be named: "Dockerfile"  , so we can obviously have only one docker file per folder at one time.
 - a docker file can be a stand-alone build or you can create a hierarchy of builds with the last one actually running it all.
 - one major pitfall that most people fail to realize and their container fails to stay up... is that you must send the container some sort of command at the end to keep the container from exiting automatically.
 - to remove containers or images, you should always use their ids (or you can be lazy and only use the first 3 characters of the id)

Terms:
 - "Dockerfile" is the definition file for what you want to build
 - "image" is really a definition file that has been compiled/built by the docker engine and is ready for use.  At this point, you might say that this maybe representative of a kernel that is not being run at the moment.
 - "container" is what we call it when we actually "run" the image and maybe our scripts are starting services or adding users to something... bash level stuff :)




## Docker Commands:

// to query all docker images:
$ docker images ls -a

// query all dicker containers:
$ docker ps -a

//copy files to/from the running container:
example: docker cp <file> <container_id>:<location>
$ docker cp threshold_testing.py $(docker ps -a -q):/opt
$ docker cp $(docker ps -a -q):/opt .

// stop a container:
$ docker stop <container_id>

// start a container.  If you needed to restart your computer.  you can use this command to get your container back up and running:
$ docker start <container_id>

// interact with the container/ like ssh'ing inside it:
$ docker exec -ti <container_id> bash

// delete/remove a container:
$ docker rm <container_id>

// remove image:
$ docker rmi <image_id>

