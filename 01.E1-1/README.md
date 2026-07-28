# 프로젝트 개요

## 실행 환경
- OS: Arch Linux
- Shell + Terminal: zsh + kitty

## 1. 터미널 실습
- 현재 위치 확인
$ pwd
/home/hay/Playground/codyssey

- 이동
hay@x13 codyssey on  main [!] 
❯ pwd
/home/hay/Playground/codyssey
hay@x13 codyssey on  main [!] 
❯ cd 01.E1-1 
hay@x13 codyssey/01.E1-1 on  main [!] 
❯ pwd
/home/hay/Playground/codyssey/01.E1-1

- 목록 확인(숨김 파일)
$ ll -a
total 12K
drwxr-xr-x  3 hay hay 4.0K Jul 28 15:13 .
drwxr-xr-x 10 hay hay 4.0K Jul 28 15:13 ..
drwxr-xr-x  6 hay hay 4.0K Jul 28 15:13 .git

- 이름변경
$ mv test test2
$ ll
total 4.0K
drwxr-xr-x 2 hay hay 4.0K Jul 28 15:18 01.E1-1
-rw-r--r-- 1 hay hay    0 Jul 28 15:15 test2

- 복사 및 이동
$ cp test2 01.E1-1
$ ls 01.E1-1
test2
$ cd 01.E1-1
$ ll
total 0
-rw-r--r-- 1 hay hay 0 Jul 28 15:19 test2
$ pwd
/home/hay/Playground/codyssey/01.E1-1

- 삭제
$ rm test2
$ ll
total 0

- 빈 파일 생성 및 파일 내용 확인
$ touch test
$ bat test
File: test   <EMPTY>

- 디렉토리 생성
$ mkdir 01.E1-1
$ ll
total 4.0K
drwxr-xr-x 2 hay hay 4.0K Jul 28 15:18 01.E1-1
-rw-r--r-- 1 hay hay    0 Jul 28 15:15 test

- 권한 변경 실습
- 변경 전
$ ll
total 4.0K
drwxr-xr-x 2 hay hay 4.0K Jul 28 15:20 01.E1-1
-rw-r--r-- 1 hay hay    0 Jul 28 15:15 test2

- 변경 후
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

## 2. Docker 실습
### 기본 점검
- 도커 버전
$ docker -v 
Docker version 29.6.2, build dfc4efb1e2

> docker info
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

### 도커 기본 운영 명령
- 이미지
$ docker images
                                                         i Info →   U  In Use
IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
mongo:latest   a706cb4e493b        1.3GB          339MB    U   

- 컨테이너
$ docker ps -a 
CONTAINER ID   IMAGE          COMMAND                  CREATED       STATUS                   PORTS     NAMES
557a927f4c8f   mongo:latest   "docker-entrypoint.s…"   7 weeks ago   Exited (0) 7 weeks ago             local-mongo

- 운영

