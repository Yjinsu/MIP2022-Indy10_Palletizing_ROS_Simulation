# How to Use Indy10 on Ubuntu 18.04?

작성자 : 21700469 유진수



<br>


## 0. ROS Setting - moveIt, Gazebo



본 프로젝트에서 UR5e를 사용하기 위해서는, ROS 설치가 선행되어야 합니다.

**[Click this link](https://github.com/Yjinsu/MIP2022-Indy10_Palletizing_ROS_Simulation/blob/main/tutorial_md/Maunal_ROS.md)**

<br>

## 1. 환경 설정

<br>

### 1. 작업 공간 생성

아래 코드를 copy & paste 하여 작업 공간을 생성합니다.

```
# Go home directory
cd ~ 


# 작업 공간 생성
mkdir -p indy_ws/src
```

### 2. src 파일 다운로드 & Catkin_make

본 Repository에 업로드 되어 있는, src 폴더 내부의 파일 전체를 다운로드합니다.
- [DownLoad Link](https://github.com/Yjinsu/MIP2022-Indy10_Palletizing_ROS_Simulation/tree/main/src)

파일 다운로드 이후, **1. 작업 공간 생성** 을 통해 만든 src 폴더 안에 다운로드한 파일 전체를 옮겨줍니다.

파일을 모두 옮긴 뒤에는, 아래의 코드를 copy & paste 합니다.

```
# Install dependencies
sudo apt update -qq
rosdep update
rosdep install --from-paths src --ignore-src -y

# Build the workspace
catkin_make
```

### 3. 경로 설정
```
# 터미널 실행 시 해당 경로에 접근, 쉘 활성화 (환경설정 초기 1회만 수행)
source devel/setup.bash 

# 현재 경로 확인이 필요하다면?
cat ~/.bashrc

#경로 수정이 필요하다면?
sudo gedit ~/.bashrc 
```


<br>


## 2. 로봇-컴퓨터 간 IP 연결 or Simulation 환경 연결

아래의 코드를 copy & paste 합니다.

```
# 로봇 연결 + 시뮬레이션 실행
roslaunch indy10_moveit_config moveit_planning_execution.launch robot_ip:=192.168.0.6

# 오직 시뮬레이션만 실행
roslaunch indy10_gazebo indy10_moveit_gazebo.launch
```

<br>

## 3. 로봇 제어

로봇 제어를 위한 코드를 실행합니다.

```
# Example
rosrun indy_driver TU_command.py
```
