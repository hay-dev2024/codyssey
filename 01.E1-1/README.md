# 프로젝트 개요

## 실행 환경
- OS: Arch Linux
- Shell + Terminal: zsh + kitty

## 1. 터미널 실습
- 현재 위치 확인
```bash
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

