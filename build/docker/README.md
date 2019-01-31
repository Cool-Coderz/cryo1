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
0) Clone this repo on your local machine using ```$ git clone https://github.com/Cool-Coderz/cryo1.git ```
1) navigate to your local copy of https://github.com/Cool-Coderz/cryo1/build/docker/images/base_image
2) run the download_files.sh file only once.  this will download the centos7 epel-release.. which is some irritating update that it needs.
 - run the file with this command ```$ ./download_files.sh```
3) once those are done... you can simply run the next script: ```$ ./rebuild_image.sh```   this initial build will take probably a good 15 minutes to run.
4) check to see if the image has been built: ```$ docker image ls```
5) now navigate to your local repo: Cool-Coderz/cryo1/build/docker/images/mod_image
6) now build this image: ```$ ./rebuild_image.sh``` this will extend the first image you created (like extending a class)... so it will only build what it needs on top of it.
7) you can run ```$ docker image ls``` again now and you should see at least one more image in the list now.
8) next lets actually run the latest image as a container: ```$ ./run_container.sh```
9) take a look at the status or your shiny new container: ```$ docker ps -a```
10)  you can now jump into the container: ```$ ./interactive_run_container.sh```   this will connect you, like ssh, into the container.  now you can do any updates you want to perform.. for testing things.
11) you can now stop and remove this container and related images if you wish.

If you can get to this point, you are doing great! and at a really happy place.  this means that we can push new docker files and you can run it right away and test new changes to the build.


## Docker images added for Django (will remove previous mod_image first):

Note: keep in mind Docker is similar to git, where you are building something big out of smaller linear pieces.

Moving forward :)
In the previous section, we had two dockerfiles that I had you build... and then you ran the last one.  We no longer want to use the second one.
We should remember that when we built and ran it... we used the following scripts in order "rebuild_image.sh" and "run_container.sh"... in order to remove this image we must reverse the process.  So, now we want to look for the container first and then the image.

since we want the container first, We can gain perspective by looking at the script we ran last: "run_container.sh" and look up the container name we ran it under.
if you found the container name == 'cc_mod', then you are on the right track.

use: "$ docker ps -a" to find any containers that exist.  you should see something like this:
$ docker ps -a
CONTAINER ID        IMAGE                              COMMAND                  CREATED             STATUS              PORTS                    NAMES
606288b36bfc        cent76_conda3_mod_run              "/opt/scripts/entryp…"   5 minutes ago       Up 4 minutes        0.0.0.0:8000->8000/tcp   cc_mod

# FIND AND STOP CONTAINER
we can see 'cc_mod' at the very end.  If you look under "STATUS" you will see either something starting with "Up # minutes" or "Exiting.."
if you see something like "Exiting...", then it means the container has already been stopped and you just need to remove it.
However if you see "Up #...." then we need to first stop it by container_id.  We can do that by using the following command (this may take 5 or more seconds):
$ docker stop 606288b36bfc

# REMOVE CONTAINER
The container we working with should be stopped by this time and show a status of "Exiting..." at this point.  Now we need to remove it, because it is a hanging thread to the image and we can't remove/rebuild the image from it until that is done.  so now use the following command (this should be faster than then stopping it):
$ docker rm 606288b36bfc

if you do a $ docker ps -a now, you should see the container gone.

# REMOVE IMAGE
Now we can remove the image we have been after.  Now to track down the image we are looking for, we look into "rebuild_image.sh" and we should see "cent76_conda3_mod_run".
using that image name we can do the following command (we should see that same image name to the left):
$ docker image ls
REPOSITORY                         TAG                 IMAGE ID            CREATED             SIZE
cent76_conda3_mod_run              latest              ac83e09d2f88        17 minutes ago      4.59GB

We can now use the image id to remove the image.  Use the following to remove it:
$ docker rmi ac83e09d2f88


## Working with the two new Django Docker images:

At this point, you should have done a "git pull origin master" or re-downloaded the repo.  To make sure we are in sync, if you do a tree on the images folder you should get this:
=============================================================================
$ tree
.
├── base_image
│   ├── Dockerfile
│   ├── download_files.sh
│   └── rebuild_image.sh
├── django_image
│   ├── Dockerfile
│   └── rebuild_image.sh
├── django_mod_image
│   ├── Dockerfile
│   ├── interactive_run_container.sh
│   ├── rebuild_image.sh
│   ├── run_container.sh
│   └── scripts
│       ├── entrypoint.sh
│       ├── run_django_project.sh
│       └── show_django.sh
└── mod_image
    ├── Dockerfile
    ├── interactive_run_container.sh
    ├── rebuild_image.sh
    ├── run_container.sh
    └── scripts
        └── entrypoint.sh

6 directories, 17 files
=============================================================================

The two folders I just added are "django_image" and "django_mod_image".

To get up and running quick:
1) cd into django_image
   - ./rebuild_image.sh
2) cd into django_mod_image
   - ./rebuild_image.sh
   - ./run_container.sh
   - ./interactive_run_container.sh
     This will get you to a shell prompt within the running container,
     and you should be in /opt/scripts
   - ./run_django_project.sh
   - navigate to the IP for the VM host that is running this docker iamges, like so:  http://127.0.0.1:8000
     You should see the default webpage for a fresh django install.

More on the way and poke around at the scripts, you get familiar with them.


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
```$ docker images ls -a```

// query all dicker containers:
```$ docker ps -a```

//copy files to/from the running container:
example: docker cp <file> <container_id>:<location>
```$ docker cp threshold_testing.py $(docker ps -a -q):/opt```
```$ docker cp $(docker ps -a -q):/opt .```

// stop a container:
```$ docker stop <container_id>```

// start a container.  If you needed to restart your computer.  you can use this command to get your container back up and running:
```$ docker start <container_id>```

// interact with the container/ like ssh'ing inside it:
```$ docker exec -ti <container_id> bash```

// delete/remove a container:
```$ docker rm <container_id>```

// remove image:
```$ docker rmi <image_id>```

