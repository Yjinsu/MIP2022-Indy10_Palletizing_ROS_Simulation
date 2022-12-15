# MIP-Robot_Control_using_ROS

<br>

## Introduction

이 Repository는 한동대학교 2022년 2학기에 진행된 기전융합설계(Mechatronics Integration Projects), <br>
**Simulation-Based Logistics Automation using Cooperative-Robot(Indy10 & UR5e)** 중, <br>
Indy10에 대한 설치 파일 및 튜토리얼로 구성되었습니다.

<br>

본 프로젝트는 산업 현장의 주요 관심사 중 하나인 **분류 공정 자동화** 를, <br>
로봇 팔을 활용하여 효과적으로 구축하기 위한 방법을 제시하기 위한 목적으로 수행되었습니다. <br>

카메라로부터 취득한 이미지 데이터로부터 박스를 인식하고, 이를 기반으로 로봇에 명령을 내리는 제어 프로그램을 구축합니다. <br>
이후, 해당 제어 프로그램을 시뮬레이션 환경에서 먼저 실행시킴으로써 안전한 자동화 공정을 구축하고자 합니다. <br>

Linux 환경에서 ROS의 Rviz, Gazebo, Moveit 패키지를 활용하여 프로그램을 작성하였습니다.

<br>

**본 프로젝트는 한동대학교 김영근 교수님의 지도아래 진행되었습니다.**

<br>

## Requirements

본 프로젝트는, Linux - ubuntu 18.04 환경에서 ROS-melodic을 활용하여 진행했습니다. <br>

**python**과 **C++** 을 활용하여 프로그램을 작성했기에, 해당 언어에 대한 활용 능력이 요구됩니다.


<br>

## Contents

* ### Tutorial: How to use Indy10
  * [Reference Link](https://github.com/Yjinsu/MIP2022-Indy10_Palletizing_ROS_Simulation/blob/main/tutorial_md/Manual_Indy10.md)

* ### Tutorial: How to use vision sensor
  * [Depth Camera](https://github.com/Yjinsu/MIP2022-Indy10_Palletizing_ROS_Simulation/blob/main/tutorial_md/Manual_Depth_Camera.md)
  * [USB Camera](https://github.com/Yjinsu/MIP2022-Indy10_Palletizing_ROS_Simulation/blob/main/tutorial_md/Manual_Webcam.md)
  
* ### Tutorial: Classification & Pick-Place (Demo)
  * [Reference Link](https://github.com/Yjinsu/MIP2022-Indy10_Palletizing_ROS_Simulation/blob/main/tutorial_md/Demo_Palletizing.md)

* ### TroubleShooting
  * [Reference Link](https://github.com/Yjinsu/MIP2022-Indy10_Palletizing_ROS_Simulation/blob/main/tutorial_md/ROS_Trouble_Shooting.md)
