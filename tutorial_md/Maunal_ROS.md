# How to Use ROS?

작성자 : 21700469 유진수

참조: https://github.com/chaochao77/ROS_neuromeka_tutorial

<br>



로봇 시뮬레이션을 위해, ROS의 설치가 요구됩니다.

본 프로젝트에서는 ROS-melodic을 사용했으며, 해당 md 파일은

로봇 시각화를 위한 **Gazebo**,

로봇의 역기구학 계산 및 제어를 위한 **moveIt** 의 설치 코드를 포함하고 있습니다.



## ROS Setting - moveIt, Gazebo



Linux에서 ctrl+alt+t 로 터미널(cmd)창을 열고 아래의 코드를 순서대로 입력합니다. ROS key 설정하는 코드입니다. <br>

- ROS 홈페이지에 접속하여 ROS key관련 최신 리스트를 받아오는 코드입니다.

  `sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'`

  `sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654`

- 최신 정보 업데이트를 진행합니다.

  `sudo apt-get update`
  
  <br>

1. **ROS 설치 코드**입니다. 터미널(cmd)에 아래와 같이 입력하시면 됩니다.

   본 튜토리얼에서는 ROS1 melodic 버전을 사용합니다.

   `sudo apt-get install ros-melodic-desktop-full`

   주의 : WIFI나 인터넷 연결 상태가 안좋거나, 랜선 자체에 Block 기능이 활성화 되어 있을 경우 완전히 다운로드 되지 않습니다.

   <br>

2. ROS 초기화 명령어 입니다. **처음 설치시**에만 사용됩니다.

- ROS 의존성 파일 설치 코드입니다.

  `sudo apt-get install python-rosdep`

  `sudo rosdep init`

  `sudo rosdep update`
  
  <br>

1. **로봇의 역기구학 계산 및 제어**를 위한 **Moveit 패키지 및 필요 파일 설치**입니다 .

   `sudo apt-get install ros-melodic-moveit`

   `sudo apt-get install ros-melodic-industrial-core`

   `sudo apt-get install ros-melodic-joint-state-publisher`

   `sudo apt-get install ros-melodic-trac-ik`

   `sudo apt-get install ros-melodic-moveit-visual-tools`

   <br>

2. 시뮬레이션을 위한 **Gazebo 설치** 입니다.

   `sudo apt-get install ros-melodic-effort-controllers`

   `sudo apt-get install ros-melodic-joint-trajectory-controller`

   <br>

3. **터미널(cmd)이 실행될 때**마다 bashrc에 **ROS관련 환경구성을 추가**해 ROS를 실행 할 때 마다 **자동적으로 환경구성을 로드**해 진행을 수월하게 합니다. 이 명령어는 한번만 해주면 됩니다.

   `echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc`

   `source ~/.bashrc`
   

<br>


