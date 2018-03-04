# Log Analysis Project

reporting tool that prints out reports based on the data in the database.

## Prerequisites

* Download [Python 3.0](https://www.python.org/downloads/) and install.
* Download [VirtualBox](https://www.virtualbox.org/wiki/Downloads) platform package for your operating system and install.
* Download [Vagrant](https://www.vagrantup.com/downloads.html) and install. Windows users may be asked to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.
* Download [Vagrantfile](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f73b_vagrantfile/vagrantfile) configuration file and [database data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Put it into a new directory on your computer. Unzip **newsdata.zip**
* Using terminal, navigate to directory, containing **Vagrantfile** and run:

```bash
vagrant up
```

* Once vagrant is done with database setting, log-in:

```bash
vagrant ssh
```

* Next navigate to vagrant folder:

```bash
cd /vagrant
```

* To load data, use command:

```bash
psql -d news -f newsdata.sql
```

## Usage

Be sure to check the vm (virtual machine) is running (`vagrant up`), you are logged in (`vagrant ssh`) and you are in the **vagrant** directory.
Next clone repo from [Github.com](https://github.com/Tylenis/log_analysis_project.git):

```bash

git clone https://github.com/Tylenis/log_analysis_project.git
```

Navigate to **log_analysis_project** folder:

```bash
cd log_analysis_project
```

Run **log_analysis.py** file with following command:

```bash
python log_analysis.py
```
