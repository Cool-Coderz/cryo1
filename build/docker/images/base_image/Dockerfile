FROM centos:7.6.1810

# Define en_US.
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_MESSAGES en_US.UTF-8

#wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
COPY epel-release-latest-7.noarch.rpm /tmp
RUN rpm -ivh /tmp/epel-release-latest-7.noarch.rpm \
    && yum install -y dbus sudo cronie ntp ntpdate git wget curl bzip2 unzip ca-certificates emacs vim nano screen multitail tree \
    && yum clean all
    
#wget https://repo.continuum.io/archive/Anaconda3-2018.12-Linux-x86_64.sh
COPY Anaconda3-2018.12-Linux-x86_64.sh /tmp
RUN echo "Installing Anaconda 3 (py3.7.1)" \
    && bash /tmp/Anaconda3-2018.12-Linux-x86_64.sh -b -p /opt/anaconda3 \
    && rm /tmp/Anaconda3-2018.12-Linux-x86_64.sh

### Set path to conda
ENV PATH /opt/anaconda3/bin:$PATH
