# 프로젝트 개요

## 실행 환경

- OS: Arch Linux
- Shell + Terminal: zsh + kitty

---

## 1. 터미널 실습

### 현재 위치 확인

```bash
$ pwd
/home/hay/Playground/codyssey
```

### 이동

```bash
$ pwd
/home/hay/Playground/codyssey

$ cd 01.E1-1

$ pwd
/home/hay/Playground/codyssey/01.E1-1
```

### 목록 확인 (숨김 파일)

```bash
$ ll -a
total 12K
drwxr-xr-x  3 hay hay 4.0K Jul 28 15:13 .
drwxr-xr-x 10 hay hay 4.0K Jul 28 15:13 ..
drwxr-xr-x  6 hay hay 4.0K Jul 28 15:13 .git
```

### 이름 변경

```bash
$ mv test test2

$ ll
total 4.0K
drwxr-xr-x 2 hay hay 4.0K Jul 28 15:18 01.E1-1
-rw-r--r-- 1 hay hay    0 Jul 28 15:15 test2
```

### 복사 및 이동

```bash
$ cp test2 01.E1-1

$ ls 01.E1-1
test2

$ cd 01.E1-1

$ ll
total 0
-rw-r--r-- 1 hay hay 0 Jul 28 15:19 test2

$ pwd
/home/hay/Playground/codyssey/01.E1-1
```

### 삭제

```bash
$ rm test2

$ ll
total 0
```

### 빈 파일 생성 및 파일 내용 확인

```bash
$ touch test

$ bat test
File: test   <EMPTY>
```

### 디렉토리 생성

```bash
$ mkdir 01.E1-1

$ ll
total 4.0K
drwxr-xr-x 2 hay hay 4.0K Jul 28 15:18 01.E1-1
-rw-r--r-- 1 hay hay    0 Jul 28 15:15 test
```

### 권한 변경 실습

#### 변경 전

```bash
$ ll
total 4.0K
drwxr-xr-x 2 hay hay 4.0K Jul 28 15:20 01.E1-1
-rw-r--r-- 1 hay hay    0 Jul 28 15:15 test2
```

#### 변경 후

```bash
$ chmod 600 test2

$ ll
total 4.0K
drwxr-xr-x 2 hay hay 4.0K Jul 28 15:20 01.E1-1
-rw------- 1 hay hay    0 Jul 28 15:15 test2

$ chmod 700 01.E1-1

$ ll
total 4.0K
drwx------ 2 hay hay 4.0K Jul 28 15:20 01.E1-1
-rw------- 1 hay hay    0 Jul 28 15:15 test2
```

---

## 2. Docker 실습

### 기본 점검

#### 도커 버전

```bash
$ docker -v
Docker version 29.6.2, build dfc4efb1e2
```

#### docker info

```bash
$ docker info
Client:
 Version:    29.6.2
 Context:    default
 Debug Mode: false
 Plugins:
  compose: Docker Compose (Docker Inc.)
    Version:  5.3.1
    Path:     /usr/lib/docker/cli-plugins/docker-compose

Server:
 Containers: 1
  Running: 0
  Paused: 0
  Stopped: 1
 Images: 1
 Server Version: 29.6.2
 Storage Driver: overlayfs
  driver-type: io.containerd.snapshotter.v1
 Logging Driver: json-file
 Cgroup Driver: systemd
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
 CDI spec directories:
  /etc/cdi
  /var/run/cdi
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: aad11006b869517fcd3009450b6f82da282e1a9b.m
 runc version:
 init version: de40ad0
 Security Options:
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 7.1.5-arch1-1
 Operating System: Arch Linux
 OSType: linux
 Architecture: x86_64
 CPUs: 12
 Total Memory: 30.57GiB
 Name: x13
 ID: 87e77755-daa7-40af-a773-d1f1fce01210
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Username: haydev2024
 Experimental: false
 Insecure Registries:
  127.0.0.0/8
  ::1/128
 Live Restore Enabled: false
 Firewall Backend: iptables
  EnableUserlandProxy: true
  UserlandProxyPath: /usr/bin/docker-proxy
```

### 도커 기본 운영 명령

#### 이미지

```bash
$ docker images

                                                         i Info →   U  In Use
IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
mongo:latest   a706cb4e493b        1.3GB          339MB    U
```

#### 컨테이너 기본

```bash
$ docker ps -a

CONTAINER ID   IMAGE          COMMAND                  CREATED       STATUS                   PORTS     NAMES
557a927f4c8f   mongo:latest   "docker-entrypoint.s…"   7 weeks ago   Exited (0) 7 weeks ago             local-mongo
```

#### 컨테이너 실행 실습
- hello-world
```bash
$ docker run hello-world                                      
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete 
d5e71e642bf5: Download complete 
Digest: sha256:c3cbe1cc1aa588a64951ac6286e0df7b27fe2e6324b1001c619bb358770c0178
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

- ubuntu
```bash
$ docker run -it ubuntu bash                                  
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
a3679419df18: Pull complete 
ed819469700f: Pull complete 
e16351a257e4: Download complete 
Digest: sha256:3131b4cc82a783df6c9df078f86e01819a13594b865c2cad47bd1bca2b7063bb
Status: Downloaded newer image for ubuntu:latest
root@76957de74720:/# ls
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
root@76957de74720:/# pwd
/
root@76957de74720:/# echo "hello world!"
hello world!
root@76957de74720:/# exit
exit
```
#### 컨테이너 종료/유지 실습
- 백그라운드로 컨테이너 띄우기
```bash
$ docker run -dit --name test-ubuntu ubuntu bash              
943a3096b7454966e09d3519b1b95af9c970a4706df922961eeaa4041658963f
```

```bash
$ docker ps -a                                  
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS                    PORTS     NAMES
943a3096b745   ubuntu         "bash"                   7 seconds ago   Up 7 seconds                        test-ubuntu
76957de74720   ubuntu         "bash"                   22 hours ago    Exited (0) 22 hours ago             sleepy_golick
15e67a53d0bc   hello-world    "/hello"                 25 hours ago    Exited (0) 25 hours ago             modest_keller
557a927f4c8f   mongo:latest   "docker-entrypoint.s…"   8 weeks ago     Exited (0) 7 weeks ago              local-mongo
```

```bash
$ docker attach test-ubuntu 
root@943a3096b745:/# pwd
/
root@943a3096b745:/# echo "hello world!"
hello world!
root@943a3096b745:/# exit
exit
```

```bash
$ docker ps -a             
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS                      PORTS     NAMES
943a3096b745   ubuntu         "bash"                   About a minute ago   Exited (0) 12 seconds ago             test-ubuntu
76957de74720   ubuntu         "bash"                   22 hours ago         Exited (0) 22 hours ago               sleepy_golick
15e67a53d0bc   hello-world    "/hello"                 25 hours ago         Exited (0) 25 hours ago               modest_keller
557a927f4c8f   mongo:latest   "docker-entrypoint.s…"   8 weeks ago          Exited (0) 7 weeks ago                local-mongo

```

```bash
$ docker start test-ubuntu
test-ubuntu
```

```bash
$ docker exec -it test-ubuntu bash   
root@943a3096b745:/# pwd
/
root@943a3096b745:/# whoami
root
root@943a3096b745:/# exit
exit
```

```bash
$ docker ps                       
CONTAINER ID   IMAGE     COMMAND   CREATED        STATUS          PORTS     NAMES
943a3096b745   ubuntu    "bash"    21 hours ago   Up 27 seconds             test-ubuntu
```

```bash
$ docker logs test-ubuntu
root@943a3096b745:/# pwd
/
root@943a3096b745:/# echo "hello world!"
hello world!
root@943a3096b745:/# exit
exit
```

```bash
$ docker stats
CONTAINER ID   NAME          CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O        PIDS
943a3096b745   test-ubuntu   0.00%     13.04MiB / 30.57GiB   0.04%     4.75kB / 126B   13.7MB / 4.1kB   1
```

```bash
$ bat html/index.html 
─────┬──────────────────────────────────────────────────────────────────────────────────────────
     │ File: html/index.html
─────┼──────────────────────────────────────────────────────────────────────────────────────────
   1 │ <!DOCTYPE html>
   2 │ <html>
   3 │     <head>
   4 │         <meta charset="UTF-8">
   5 │         <title>안녕 난 뽀로로야</title>
   6 │     </head>
   7 │     <body>
   8 │         <h1>안녕 난 뽀로로야!!</h1>
   9 │         <p>뽀롱뽀롱~~~</p>
  10 │     </body>
  11 │ </html>
─────┴───────
```

```bash
$ bat Dockerfile     
─────┬──────────────────────────────────────────────────────────────────────────────────────────
     │ File: Dockerfile
─────┼──────────────────────────────────────────────────────────────────────────────────────────
   1 │ FROM nginx:latest
   2 │ 
   3 │ COPY html/ /usr/share/nginx/html
   4 │ 

```

```bash
$ docker build -t my-nginx .
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  3.584kB
Step 1/2 : FROM nginx:latest
latest: Pulling from library/nginx
d26f27cc8c41: Pulling fs layer
82454cdbf456: Pulling fs layer
b6698f04e005: Pulling fs layer
3c7ab7949321: Pulling fs layer
cacfcdd01f30: Pulling fs layer
2bedaf25031a: Pulling fs layer
062e450697fa: Pulling fs layer
d26f27cc8c41: Download complete
3c7ab7949321: Download complete
cacfcdd01f30: Download complete
b6698f04e005: Download complete
2bedaf25031a: Download complete
062e450697fa: Download complete
6c496f5b5050: Download complete
82454cdbf456: Download complete
ea1d76ccc2c6: Download complete
062e450697fa: Pull complete
3c7ab7949321: Pull complete
82454cdbf456: Pull complete
d26f27cc8c41: Pull complete
cacfcdd01f30: Pull complete
b6698f04e005: Pull complete
2bedaf25031a: Pull complete
Digest: sha256:5a88c9c45479443d7be2eadc894b4ed0a9801bae03d97a5760ae13b5c2005942
Status: Downloaded newer image for nginx:latest
 ---> 5a88c9c45479
Step 2/2 : COPY html/ /usr/share/nginx/html
 ---> df71344daa9c
Successfully built df71344daa9c
Successfully tagged my-nginx:latest
```

```bash
$ docker images             
                                                                            i Info →   U  In Use
IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-world:latest   c3cbe1cc1aa5       25.9kB         9.49kB    U   
mongo:latest         a706cb4e493b        1.3GB          339MB    U   
my-nginx:latest      df71344daa9c        238MB         63.1MB        
nginx:latest         5a88c9c45479        241MB           66MB        
ubuntu:latest        3131b4cc82a7        161MB         45.3MB    U
```

```bash
$ docker run -d -p 8080:80 --name my-nginx-container my-nginx                   
9938381a1eed62d5287250bd677111f0196d320ca0352c92a3a831b8ec80e4bc
```

```bash
$ docker ps                                                  
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS          PORTS                                     NAMES
9938381a1eed   my-nginx   "/docker-entrypoint.…"   3 seconds ago   Up 3 seconds    0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   my-nginx-container
943a3096b745   ubuntu     "bash"                   22 hours ago    Up 41 minutes                                             test-ubuntu
```

```bash
$ curl http://localhost:8080
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>안녕 난 뽀로로야</title>
    </head>
    <body>
        <h1>안녕 난 뽀로로야!!</h1>
        <p>뽀롱뽀롱~~~</p>
    </body>
</html>
```


