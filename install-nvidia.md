# For Ubunutu 18.04

### 1) Install nvidia-drivers

```ubuntu-drivers devices```

```sudo ubuntu-drivers autoinstall```

--> reboot

--> ```nvidia-smi``` should work now.

### 2) Install nvidia-docker

--> Docker has to be installed. Check if ```docker``` works.

~~~
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
sudo tee /etc/apt/sources.list.d/nvidia-docker.list
~~~
 
 
 ```sudo apt-get update```
 
 
 ```sudo apt-get install -y nvidia-docker2```
 
 ```sudo pkill -SIGHUP dockerd```
 
 --> ```docker run --runtime=nvidia --rm nvidia/cuda:9.0-base nvidia-smi``` should work now.
