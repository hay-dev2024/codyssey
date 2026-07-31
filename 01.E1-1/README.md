# 프로젝트 개요

## 실행 환경

- OS: Arch Linux
- Shell + Terminal: zsh + kitty
- Git: 2.55.0
- Docker: 29.6.2
---

## 1. 터미널 실습

#### 절대 경로와 상대 경로
- **절대 경로(Absolute Path)**: 루트 디렉터리(`/`)부터 시작하는 전체 경로이다.
- **상대 경로(Relative Path)**: 현재 작업 중인 디렉터리를 기준으로 하는 경로이다.

예를 들어 현재 위치가 `/home/hay/Playground/codyssey`라면,

| 절대 경로 | 상대 경로 |
|-----------|-----------|
| `/home/hay/Playground/codyssey/01.E1-1` | `01.E1-1` |
| `/home/hay` | `../../` |
| `/home/hay/Downloads` | `../../Downloads` |

#### 자주 사용하는 상대 경로
- `.` : 현재 디렉터리
- `..` : 상위 디렉터리

### 현재 위치 확인

현재 작업 중인 디렉터리의 절대 경로를 확인한다.
```bash
$ pwd
/home/hay/Playground/codyssey
```

### 이동

`cd` 명령으로 원하는 디렉터리로 이동한다.
```bash
$ pwd
/home/hay/Playground/codyssey

$ cd 01.E1-1

$ pwd
/home/hay/Playground/codyssey/01.E1-1
```

### 목록 확인 (숨김 파일)

`ll(ls -l)` 명령으로 파일 목록을 확인하고, `-a` 옵션으로 숨김 파일까지 함께 출력한다.
```bash
$ ll -a
total 12K
drwxr-xr-x  3 hay hay 4.0K Jul 28 15:13 .
drwxr-xr-x 10 hay hay 4.0K Jul 28 15:13 ..
drwxr-xr-x  6 hay hay 4.0K Jul 28 15:13 .git
```

### 이름 변경

`mv` 명령으로 파일의 이름을 변경한다.
```bash
$ mv test test2

$ ll
total 4.0K
drwxr-xr-x 2 hay hay 4.0K Jul 28 15:18 01.E1-1
-rw-r--r-- 1 hay hay    0 Jul 28 15:15 test2
```

### 복사 및 이동
`cp` 명령으로 파일을 복사하고, `ls`, `ll`, `pwd` 명령으로 결과를 확인한다.
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
`rm` 명령으로 파일을 삭제한다.
```bash
$ rm test2

$ ll
total 0
```

### 빈 파일 생성 및 파일 내용 확인

`touch`로 빈 파일을 생성하고, `bat`으로 파일 내용을 확인한다.

> **참고:** `bat`은 `cat`과 비슷한 기능을 제공하며, 문법 강조와 줄 번호를 지원하는 명령어이다.
```bash
$ touch test

$ bat test
File: test   <EMPTY>
```

### 디렉토리 생성

`mkdir` 명령으로 새로운 디렉터리를 생성한다.
```bash
$ mkdir 01.E1-1

$ ll
total 4.0K
drwxr-xr-x 2 hay hay 4.0K Jul 28 15:18 01.E1-1
-rw-r--r-- 1 hay hay    0 Jul 28 15:15 test
```

### 권한 변경 실습
`chmod` 명령으로 파일과 디렉터리의 접근 권한을 변경한다.

#### 권한 숫자 의미
Linux 권한은 **읽기(Read), 쓰기(Write), 실행(Execute)** 권한의 조합으로 표현한다.

| 권한 | 값 |
|------|---:|
| Read (r) | 4 |
| Write (w) | 2 |
| Execute (x) | 1 |

권한 숫자는 각 값을 더해서 표현한다.

| 숫자 | 권한 |
|-----:|------|
| 7 | rwx (4+2+1) |
| 6 | rw- (4+2) |
| 5 | r-x (4+1) |
| 4 | r-- (4) |
| 0 | --- |

예를 들어,

- `600` : 소유자만 읽기/쓰기 가능 (`rw-------`)
- `700` : 소유자만 읽기/쓰기/실행 가능 (`rwx------`)

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
Docker가 정상적으로 설치되었는지와 실행 환경을 확인한다.

#### 도커 버전

```bash
$ docker -v
Docker version 29.6.2, build dfc4efb1e2
```

#### docker info

Docker Engine과 시스템 환경의 상세 정보를 확인한다.
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
Docker 이미지와 컨테이너를 관리하는 기본 명령을 실습한다.

#### Docker 이미지(Image)와 컨테이너(Container)
Docker 이미지는 애플리케이션 실행에 필요한 프로그램과 라이브러리, 설정 등을 포함하는 **읽기 전용 템플릿**이다.

Docker 컨테이너는 이미지를 기반으로 생성되는 **실행 중인 인스턴스**이며, 실제 프로그램이 동작하는 환경이다.

쉽게 말하면,

- **이미지(Image)** : 실행 파일(설계도)
- **컨테이너(Container)** : 실행 중인 프로그램(실체)

예를 들어 `ubuntu:latest` 이미지를 사용하여 여러 개의 Ubuntu 컨테이너를 생성할 수 있다.

#### 이미지
로컬에 저장된 Docker 이미지를 확인한다.
```bash
$ docker images

                                                         i Info →   U  In Use
IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
mongo:latest   a706cb4e493b        1.3GB          339MB    U
```

#### 컨테이너 기본
생성된 컨테이너의 상태를 확인한다.
```bash
$ docker ps -a

CONTAINER ID   IMAGE          COMMAND                  CREATED       STATUS                   PORTS     NAMES
557a927f4c8f   mongo:latest   "docker-entrypoint.s…"   7 weeks ago   Exited (0) 7 weeks ago             local-mongo
```

#### 컨테이너 실행 실습
Docker 이미지를 실행하여 컨테이너의 동작을 확인한다.

##### hello-world
Docker가 정상적으로 동작하는지 확인한다.
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
##### ubuntu
Ubuntu 컨테이너를 실행하고 Linux 명령을 사용해 본다.
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
컨테이너를 실행하고 종료, 재시작 및 접속 방법을 실습한다.

##### 백그라운드로 컨테이너 실행
`-d` 옵션을 사용하여 컨테이너를 백그라운드에서 실행한다.

```bash
$ docker run -dit --name test-ubuntu ubuntu bash              
943a3096b7454966e09d3519b1b95af9c970a4706df922961eeaa4041658963f
```

##### 전체 컨테이너 목록 확인
실행 중이거나 종료된 모든 컨테이너를 확인한다.
```bash
$ docker ps -a                                  
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS                    PORTS     NAMES
943a3096b745   ubuntu         "bash"                   7 seconds ago   Up 7 seconds                        test-ubuntu
76957de74720   ubuntu         "bash"                   22 hours ago    Exited (0) 22 hours ago             sleepy_golick
15e67a53d0bc   hello-world    "/hello"                 25 hours ago    Exited (0) 25 hours ago             modest_keller
557a927f4c8f   mongo:latest   "docker-entrypoint.s…"   8 weeks ago     Exited (0) 7 weeks ago              local-mongo
```

##### 실행 중인 컨테이너에 접속
`docker attach`를 사용하여 실행 중인 컨테이너의 메인 프로세스에 연결한다.
```bash
$ docker attach test-ubuntu 
root@943a3096b745:/# pwd
/
root@943a3096b745:/# echo "hello world!"
hello world!
root@943a3096b745:/# exit
exit
```

##### 종료된 컨테이너 확인
컨테이너가 정상적으로 종료되었는지 확인한다.
```bash
$ docker ps -a             
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS                      PORTS     NAMES
943a3096b745   ubuntu         "bash"                   About a minute ago   Exited (0) 12 seconds ago             test-ubuntu
76957de74720   ubuntu         "bash"                   22 hours ago         Exited (0) 22 hours ago               sleepy_golick
15e67a53d0bc   hello-world    "/hello"                 25 hours ago         Exited (0) 25 hours ago               modest_keller
557a927f4c8f   mongo:latest   "docker-entrypoint.s…"   8 weeks ago          Exited (0) 7 weeks ago                local-mongo

``` 

##### 종료된 컨테이너 재시작
`docker start`를 사용하여 중지된 컨테이너를 다시 실행한다.
```bash
$ docker start test-ubuntu
test-ubuntu
```

##### 실행 중인 컨테이너에 새 프로세스로 접속
`docker exec`를 사용하여 새로운 Bash 프로세스를 실행한다.
```bash
$ docker exec -it test-ubuntu bash   
root@943a3096b745:/# pwd
/
root@943a3096b745:/# whoami
root
root@943a3096b745:/# exit
exit
```
실행 후 컨테이너가 계속 동작하는지 확인한다.
```bash
$ docker ps                       
CONTAINER ID   IMAGE     COMMAND   CREATED        STATUS          PORTS     NAMES
943a3096b745   ubuntu    "bash"    21 hours ago   Up 27 seconds             test-ubuntu
```

#### attach와 exec의 차이
| 명령어 | 설명 |
|--------|------|
| `docker attach` | 실행 중인 컨테이너의 **메인 프로세스**에 연결한다. |
| `docker exec` | 실행 중인 컨테이너에서 **새로운 프로세스**를 실행한다. |

이번 실습에서는 `attach`로 기존 Bash 프로세스에 연결한 후 `exit`을 입력하여 컨테이너가 종료되었고, `exec`는 새로운 Bash 프로세스를 실행하므로 `exit`을 입력해도 컨테이너는 계속 실행된다.

<details>
<summary><strong>왜 attach는 컨테이너가 종료되고 exec는 종료되지 않을까?</strong></summary>

Docker 컨테이너는 **메인 프로세스(PID 1)** 가 실행되는 동안만 살아 있다.

- `docker attach`는 메인 프로세스(PID 1)에 연결하므로 `exit`을 입력하면 메인 프로세스가 종료되고 컨테이너도 함께 종료된다.
- `docker exec`는 메인 프로세스와 별도로 새로운 프로세스를 실행하므로, `exit`을 입력해도 새 프로세스만 종료되고 메인 프로세스는 계속 실행된다.

</details>

##### 컨테이너 로그 확인
`docker logs`를 사용하여 컨테이너의 표준 출력 로그를 확인한다.
```bash
$ docker logs test-ubuntu
root@943a3096b745:/# pwd
/
root@943a3096b745:/# echo "hello world!"
hello world!
root@943a3096b745:/# exit
exit
```

##### 실시간 리소스 모니터링
`docker stats`를 사용하여 CPU와 메모리 사용량을 실시간으로 확인한다.
```bash
$ docker stats
CONTAINER ID   NAME          CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O        PIDS
943a3096b745   test-ubuntu   0.00%     13.04MiB / 30.57GiB   0.04%     4.75kB / 126B   13.7MB / 4.1kB   1
```

#### Nginx 커스텀 이미지 실습
Dockerfile을 작성하여 커스텀 Nginx 이미지를 생성하고 실행한다.

##### HTML 파일 작성
Nginx에서 제공할 HTML 파일을 작성한다.
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
##### Dockerfile 작성
기본 Nginx 이미지에 HTML 파일을 복사하도록 Dockerfile을 작성한다.
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

##### 커스텀 이미지 빌드
Dockerfile을 기반으로 커스텀 이미지를 생성한다.
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

빌드 후 생성된 이미지를 확인한다.
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

##### 컨테이너 실행
생성한 이미지를 컨테이너로 실행하고 호스트의 8080 포트로 들어온 요청을 컨테이너의 80 포트(Nginx)로 전달하도록 포트를 매핑한다.
```bash
$ docker run -d -p 8080:80 --name my-nginx-container my-nginx                   
9938381a1eed62d5287250bd677111f0196d320ca0352c92a3a831b8ec80e4bc
```

실행 중인 컨테이너를 확인한다.
```bash
$ docker ps                                                  
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS          PORTS                                     NAMES
9938381a1eed   my-nginx   "/docker-entrypoint.…"   3 seconds ago   Up 3 seconds    0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   my-nginx-container
943a3096b745   ubuntu     "bash"                   22 hours ago    Up 41 minutes                                             test-ubuntu
```

웹 서버가 정상적으로 동작하는지 확인한다.
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

> 스크린샷 추가 예정


### 바인드 마운트 실습
호스트 디렉터리를 컨테이너와 연결하여 파일 변경 사항이 즉시 반영되는지 확인한다.

#### 바인드 마운트(Bind Mount)
바인드 마운트는 **호스트의 파일이나 디렉터리를 컨테이너 내부와 직접 연결하는 기능**이다.

호스트에서 파일을 수정하면 컨테이너 내부에도 즉시 반영되므로, 개발 환경에서 소스 코드를 실시간으로 수정할 때 자주 사용된다.

```
호스트(html/)
        │
        ▼
컨테이너(/usr/share/nginx/html)
```

##### 바인드 마운트 컨테이너 실행
호스트의 `html` 디렉터리를 Nginx 웹 루트와 연결한다.
```bash
$ docker run -d -p 8081:80 --name nginx-bind -v $(pwd)/html:/usr/share/nginx/html nginx:latest
52f784356f5fad80feb597d5f81364df3d18b0f40aa7bd31136a801e3e099b19
```
##### 초기 동작 확인
웹 페이지에 접근하여 결과를 확인한다.
```bash
$ curl http://localhost:8081
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.31.3</center>
</body>
</html>
```

##### 파일 수정 시도
호스트에서 HTML 파일을 생성하려 했지만 권한 문제로 실패하였다.

```bash
$ echo "<h1>바인드 마운트 테스트</h1>" > html/index.html
zsh: permission denied: html/index.html

$ sudo echo "<h1>바인드 마운트 테스트</h1>" > html/index.html
zsh: permission denied: html/index.html
```

현재 디렉터리의 소유자를 확인한다.
```bash
$ ls -la html/
total 8
drwxr-xr-x 2 root root 4096 Jul 31 10:59 .
drwxr-xr-x 4 hay  hay  4096 Jul 31 11:03 ..
```

작업 디렉터리를 확인한다.
```bash
$ ll nginx-mission
total 8.0K
-rw-r--r-- 1 hay hay   53 Jul 30 15:32 Dockerfile
drwxr-xr-x 2 hay hay 4.0K Jul 30 15:28 html
```

##### 기존 컨테이너 종료
기존 바인드 마운트 컨테이너를 삭제한다.

```bash
$ docker stop nginx-bind && docker rm nginx-bind
nginx-bind
nginx-bind
```

##### 권한 수정
호스트 디렉터리의 소유권을 현재 사용자에게 변경한다.

```bash
$ sudo chown -R $USER:$USER html
[sudo] password for hay:
```

<details>
<summary><strong>chown 명령어 설명</strong></summary>

#### `chown` 명령어

`chown`은 파일이나 디렉터리의 **소유자(owner)** 와 **소유 그룹(group)** 을 변경하는 명령이다.

- `sudo` : 관리자(root) 권한으로 명령 실행
- `chown` : 파일 또는 디렉터리의 소유자와 그룹 변경
- `-R` : 하위 디렉터리와 파일까지 재귀적으로 적용
- `$USER:$USER` : 현재 로그인한 사용자를 소유자와 소유 그룹으로 지정

즉, `sudo chown -R $USER:$USER html`은 `html` 디렉터리와 그 안의 모든 파일 및 디렉터리의 소유자와 소유 그룹을 현재 사용자로 변경하는 명령이다.

</details>


변경 결과를 확인한다.
```bash
$ ls -la html/
total 8
drwxr-xr-x 2 hay hay 4096 Jul 31 10:59 .
drwxr-xr-x 4 hay hay 4096 Jul 31 11:07 ..
```

##### HTML 파일 생성
새로운 HTML 파일을 작성한다.

```bash
$ cat > html/index.html << 'EOF'
∙ <!DOCTYPE html>
∙ <html>
∙       <head><meta charset="UTF charset="UTF-8"><title>바인드 마운트 테스트</title></head>
∙ <body><h1>바인드 마운트 테스트</h1></body>
∙ </html>
∙ EOF
```

작성된 파일을 확인한다.
```bash
$ bat html/index.html
─────┬──────────────────────────────────────────────────────────────────────────────────────────
     │ File: html/index.html
─────┼──────────────────────────────────────────────────────────────────────────────────────────
   1 │ <!DOCTYPE html>
   2 │ <html>
   3 │     <head><meta charset="UTF charset="UTF-8"><title>바인드 마운트 테스트</title></head>
   4 │ <body><h1>바인드 마운트 테스트</h1></body>
   5 │ </html>
─────┴──────────────────────────────────────────────────────────────────────────────────────────
```
##### 컨테이너 재실행
수정된 디렉터리를 다시 바인드 마운트한다.

```bash
$ docker run -d -p 8081:80 --name nginx-bind -v $(pwd)/html:/usr/share/nginx/html nginx:latest
e2cfbba3f22b4fcd66d53a0b854e297cd0665749505c42afee384d9cb83b555a
```

웹 페이지가 정상적으로 출력되는지 확인한다.
```bash
$ curl http://localhost:8081
<!DOCTYPE html>
<html>
    <head><meta charset="UTF charset="UTF-8"><title>바인드 마운트 테스트</title></head>
<body><h1>바인드 마운트 테스트</h1></body>
</html>
```

##### HTML 수정
호스트에서 HTML 파일을 수정한다.

```bash
$ nvim html/index.html
```

수정된 내용을 확인한다.
```bash
$ bat html/index.html
─────┬──────────────────────────────────────────────────────────────────────────────────────────
     │ File: html/index.html
─────┼──────────────────────────────────────────────────────────────────────────────────────────
   1 │ <!DOCTYPE html>
   2 │ <html>
   3 │     <head>
   4 │         <meta charset="UTF-8">
   5 │         <title>바인드 마운트 테스트</title>
   6 │     </head>
   7 │     <body>
   8 │         <h1>바인드 마운트 테스트</h1>
   9 │     </body>
  10 │ </html>
─────┴──────────────────────────────────────────────────────────────────────────────────────────
```

바인드 마운트를 사용하였기 때문에 컨테이너를 재시작하지 않아도 변경 사항이 즉시 반영되었다.

```bash
$ curl http://localhost:8081
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>바인드 마운트 테스트</title>
    </head>
    <body>
        <h1>바인드 마운트 테스트</h1>
    </body>
</html>
```

### 볼륨 생성 및 영속성 확인
Docker Volume을 생성하여 컨테이너를 삭제해도 데이터가 유지되는지 확인한다.

#### Docker Volume
Docker Volume은 **Docker가 직접 관리하는 영구 저장 공간**이다.

컨테이너를 삭제해도 Volume은 삭제되지 않으며, 동일한 Volume을 다른 컨테이너에 연결하면 기존 데이터를 그대로 사용할 수 있다.

따라서 데이터베이스, 업로드 파일 등 **컨테이너보다 오래 유지되어야 하는 데이터**를 저장할 때 주로 사용한다.

#### Bind Mount와 Volume의 차이
| Bind Mount | Volume |
|------------|--------|
| 호스트의 특정 디렉터리를 직접 연결 | Docker가 관리하는 저장 공간 |
| 호스트의 파일 구조를 그대로 사용 | Docker가 전용 저장 공간을 관리 |
| 파일 변경 사항이 즉시 반영되어 개발 환경에 적합 | 데이터 영속성이 중요할 때 적합 |
| 호스트 디렉터리에 의존 | 컨테이너와 독립적으로 관리 가능 |

##### 볼륨 생성
새로운 Docker Volume을 생성한다.

```bash
$ docker volume create nginx-vol
nginx-vol
```
생성된 볼륨 목록을 확인한다.
```bash
$ docker volume ls
DRIVER    VOLUME NAME
local     4509c52364061bbbac1e4b492ab3cc1bc674a2ad3f819dcf05f33f8793de68ad
local     b4187af3cb3c28f19202e776e3c59d6dce7633933bd8c4a2a7d3d5903656c41c
local     f92be2a000efeb0c1f0ff4f63090c4bb0afb56800945179fc681aaf4a2cdea54
local     ffb9ed1b0d0bfdc5c41e7b9fdf23e0206ae5e393c959a7afa3aba0d8d4b9d019
local     nginx-vol
```

볼륨 정보를 확인한다.
```bash
$ docker volume inspect nginx-vol
[
    {
        "CreatedAt": "2026-07-31T11:25:15+09:00",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/nginx-vol/_data",
        "Name": "nginx-vol",
        "Options": null,
        "Scope": "local"
    }
]
```

##### 볼륨을 사용하는 컨테이너 실행
생성한 Volume을 Nginx 웹 루트에 연결한다.

```bash
$ docker run -d --name nginx-vol-test -p 8082:80 -v nginx-vol:/usr/share/nginx/html nginx
1dd5a9c2d8d871f7449e4c446d93f8e98f470a9e80509bf13e8bbd2aa605961d
```

컨테이너 내부에서 HTML 파일을 생성한다.
```bash
$ docker exec nginx-vol-test sh -c 'echo "<h1>볼륨 테스트</h1>" > /usr/share/nginx/html/index.html'
```

웹 페이지를 확인한다.
```bash
$ curl http://localhost:8082
<h1>볼륨 테스트</h1>
```

##### 영속성 확인
컨테이너를 삭제한다.
```bash
$ docker rm -f nginx-vol-test
nginx-vol-test
```

삭제 여부를 확인한다.
```bash
$ docker ps -a | grep nginx-vol-test
```

동일한 Volume으로 새로운 컨테이너를 실행한다.
```bash
$ docker run -d --name nginx-vol-test2 -p 8082:80 -v nginx-vol:/usr/share/nginx/html nginx
08cf48860e4fb94175c458ed9a985d6d221baa5afe7f774b1a488005bab644f0
```

기존 데이터가 유지되는지 확인한다.
```bash
$ curl http://localhost:8082
<h1>볼륨 테스트</h1>
```

---

## Git 설정

Git 버전 확인
```bash
$ git -v       
git version 2.55.0
```

Git 사용자 정보와 원격 저장소 설정을 확인한다.
```bash
$ git config --list
user.email=OOOOO@gmail.com
user.name=hay-dev2024
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
remote.origin.url=git@github.com:hay-dev2024/codyssey.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
```

## GitHub 연동
GitHub 저장소와 정상적으로 연동되었음을 확인한다.

### GitHub 저장소 스크린샷

> 추후 추가 예정

---


## 트러블 슈팅
실습 과정에서 발생한 문제와 해결 방법을 정리하였다.

### 1. HTML 파일이 없어 403 Forbidden 발생
```bash
$ curl http://localhost:8081
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.31.3</center>
</body>
</html>
```
#### 원인
바인드 마운트한 디렉터리에 `index.html` 파일이 존재하지 않았다.

#### 해결
```bash
$ cat > html/index.html << 'EOF'
∙ <!DOCTYPE html>
∙ <html>
∙       <head><meta charset="UTF charset="UTF-8"><title>바인드 마운트 테스트</title></head>
∙ <body><h1>바인드 마운트 테스트</h1></body>
∙ </html>
∙ EOF
```

### 2. 바인드 마운트 디렉터리 권한 문제

#### 문제

```bash
$ echo "<h1>바인드 마운트 테스트</h1>" > html/index.html
zsh: permission denied: html/index.html

$ sudo echo "<h1>바인드 마운트 테스트</h1>" > html/index.html
zsh: permission denied: html/index.html
```

#### 원인
`html` 디렉터리의 소유자가 `root`여서 일반 사용자가 파일을 수정할 수 없었다.

#### 해결

```bash
$ sudo chown -R $USER:$USER html
[sudo] password for hay:
```

변경 후 권한을 확인하였다.
```bash
$ ls -la html/
total 8
drwxr-xr-x 2 hay hay 4096 Jul 31 10:59 .
drwxr-xr-x 4 hay hay 4096 Jul 31 11:07 ..
```

## 실습 완료
이번 실습을 통해 Linux 기본 명령어, Docker 이미지 및 컨테이너 관리, Dockerfile 작성, 포트 매핑, 바인드 마운트, Docker Volume, Git 설정 및 GitHub 연동을 수행하였다.
