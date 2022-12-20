# How to Use Indy10 on Ubuntu 18.04?

작성자 : 21700469 유진수

참조 : https://github.com/chaochao77/ROS_neuromeka_tutorial

<br>


## 0. ROS Setting - moveIt, Gazebo

Linux에서 ctrl+alt+t 로 터미널(cmd)창을 열고 아래의 코드를 순서대로 입력합니다. ROS key 설정하는 코드입니다. <br>

- ROS 홈페이지에 접속하여 ROS key관련 최신 리스트를 받아오는 코드입니다.

  `sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'`

  `sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654`

- 최신 정보 업데이트를 진행합니다.

  `sudo apt-get update`

1. **ROS 설치 코드**입니다. 터미널(cmd)에 아래와 같이 입력하시면 됩니다.

   본 튜토리얼에서는 ROS1 melodic 버전을 사용합니다.

   `sudo apt-get install ros-melodic-desktop-full`

   주의 : WIFI나 인터넷 연결 상태가 안좋거나, 랜선 자체에 Block 기능이 활성화 되어 있을 경우 완전히 다운로드 되지 않습니다.

2. ROS 초기화 명령어 입니다. **처음 설치시**에만 사용됩니다.

- ROS 의존성 파일 설치 코드입니다.

  `sudo apt-get install python-rosdep`

  `sudo rosdep init`

  `sudo rosdep update`

1. **로봇의 역기구학 계산 및 제어**를 위한 **Moveit 패키지 및 필요 파일 설치**입니다 .

   `sudo apt-get install ros-melodic-moveit`

   `sudo apt-get install ros-melodic-industrial-core`

   `sudo apt-get install ros-melodic-joint-state-publisher`

   `sudo apt-get install ros-melodic-trac-ik`

   `sudo apt-get install ros-melodic-moveit-visual-tools`

2. 시뮬레이션을 위한 **Gazebo 설치** 입니다.

   `sudo apt-get install ros-melodic-effort-controllers`

   `sudo apt-get install ros-melodic-joint-trajectory-controller`

3. **터미널(cmd)이 실행될 때**마다 bashrc에 **ROS관련 환경구성을 추가**해 ROS를 실행 할 때 마다 **자동적으로 환경구성을 로드**해 진행을 수월하게 합니다. 이 명령어는 한번만 해주면 됩니다.

   `echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc`

   `source ~/.bashrc`
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
rosrun indy_driver Robot_Controller.py
```
