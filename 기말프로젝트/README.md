# 2D-GameProgramming Term Project

 1 . 게임의 소개

​	제목 -반격왕

  	 게임의 목적
		각 스테이지에서 플레이어를 공격하는 적들을 제압하고 클리어한다.
 	  게임의 방법
		키보드를 이용하여 이동과 점프, 그리고 방어 자세를 취한다
		적들의 공격을 방어 자세를 통해 막아 내게 된다면, 마우스를 이용한 반격 공격으로
		적들을 물리 칠 수 있다.
		스테이지는 총 5개로 구성되어있으며, 각 스테이지의 모든 적들을 제압 할 시 다음 스테이지로
		넘어 갈 수 있는 통로가 생성된다. 5개의 스테이지를 모두 클리어 하게 된다면, 5스테이지 까지의
		클리어 시간을 체크하고 기록 할 수 있는 랭크화면으로 넘어간다.
​		플레이어의 반격 공격은 적의 공격을 그대로 사용한다.
​		예를 들어 적이 포물선으로 던지는 수류탄을 사용할 경우 플레이어가 반격 공격 사용시 
​		적이 던진 수류탄을 공격 무기로 삼는다.
​		플레이어는 총 5개의 체력을 가지며, 반격에 실패 할 시 플레이어는 체력을 하나 소진 하게 된다.
​		플레이어의 체력이 모두 소진된다면 게임종료 화면으로 넘어간다.

2. GameState
   
   - LogoState
	
   - MainState
	
   - GameState_1 ~ GameState_5
	
   - DeadState
	
   - ClearState
	
   - RankState
	
	
	
3. GameState 소개

   

   ![diagram_final](https://user-images.githubusercontent.com/71081825/94271392-87f17f80-ff7c-11ea-89d0-f8bc7231bc2d.png)


      - LogoState : 게임 실행 시 게임 메인 화면으로 넘어가기 전 나오는 로고 창
      -  MainState : 게임 메인 화면, 게임 플레이 와 랭킹으로 넘어 갈 수 있다.
         Play , Rank 버튼이 존재한다. 마우스 클릭시 각 State로 넘어가게 된다.

   - GameState_1 : 스테이지 1 게임 화면
     적들과 플레이어, 장애물이 위치한다. 적들을 모두 제압 할 시, 포탈이 생기며 포탈 위치에서 w 키보드 입력시 다음 스테이지로 넘어간다.
   - GameState_2 : 스테이지 2 게임 화면
     적들과 플레이어, 장애물이 위치한다. 적들을 모두 제압 할 시, 포탈이 생기며 포탈 위치에서 w 키보드 입력시 다음 스테이지로 넘어간다.

   - GameState_3 : 스테이지 3 게임 화면
     적들과 플레이어, 장애물이 위치한다. 적들을 모두 제압 할 시, 포탈이 생기며 포탈 위치에서 w 키보드 입력시 다음 스테이지로 넘어간다.

   - GameState_4 : 스테이지 4 게임 화면	
     적들과 플레이어, 장애물이 위치한다. 적들을 모두 제압 할 시, 포탈이 생기며 포탈 위치에서 w 키보드 입력시 다음 스테이지로 넘어간다.

   - GameState_5 : 스테이지 5 게임 화면
     적들과 플레이어, 장애물이 위치한다. 적들을 모두 제압 할 시 ClearState로 넘어간다.

   - DeadState : 플레이어 사망 시 나오게 된다. 메인 화면으로 넘어갈 수 있다.
     GoToMain 버튼이 존재한다. 클릭 할 시 메인 화면으로 넘어간다.

   - ClearState : 플레이어가 스테이지 5까지 클리어하게 된다면 나오게 된다. 메인 화면으로 넘어갈 수있다.
     클리어 타임이 표시되어 있으며, 이니셜 입력이 가능하다. GoToMain 버튼과 Rank 버튼이 존재하며 클릭 시 넘어간다.

   - RankSatate: 랭킹을 확인 할 수 있다. 메인 화면으로 넘어 갈 수있다.
      기록된 랭킹을 확인 할 수있다. GoToMain 마우스 클릭 시 메인화면으로 넘어 갈 수 있다.

      ​	

      *GameState_1 ~ Game_State5

      키보드 이벤트 :  w a s d , Spacebar  ,Lshift

      ​	a-> 플레이어 왼쪽 이동

      ​	d-> 플레이어 오른쪽 이동

      ​    w-> 플레이어 포탈 이동

      ​	spacebar -> 플레이어 점프

      ​	s + spacebar - > 플레이어 아래 층으로 내려가기

      ​    Lshift -> 플레이어 방어 자세 

      마우스 이벤트 : 왼쪽 버튼

      ​	플레이어 방어자세를 취한후 적의 공격을 방어 햇다면 1초안에 반격이 가능하다

      ​	1초 안에 마우스 클릭을 이용해 플레이어가 공격을 할 수 있다.

   4.필요한 기술

   - 투사체 움직임, 충돌처리 : 직선으로 움직이는 투사체와, 포물선으로 움직이는 투사체의 움직임을 구현해야 하며,  사물과의 충돌과 플레이어와의 충돌 또는 적과의 충돌을 알 수있는 충돌 처리가 필요하다.

   - 플레이어가 적의 근처에 도달하게 되면 적이 플레이어를 자동으로 감지 하는 기술이 필요하다.

   - 투사체의 포물선 운동: 공튀기기 를 학습하였기 때문에 각도를 통한 포물선 운동을 이용 할 수있다.

     

     

     5. 인게임 예시

     ![인게임 예시](https://user-images.githubusercontent.com/71081825/95839248-c27d5980-0d7d-11eb-84cd-f8a5f24e9d04.png)

     6.개발일정

![일정](https://user-images.githubusercontent.com/71081825/95839306-d4f79300-0d7d-11eb-988c-55561fd175c7.png)

## 2차 발표 

`게임 간단한 소개`

  게임 반격왕은 적(몬스터)들의 공격을 쉴드로 막아낸 뒤 적들의 공격을 마우스 이벤트를 통해 반격하  여 제거하는 게임입니다.

`진행 상황`
![주차별 진행 상황](https://user-images.githubusercontent.com/71081825/99965331-1301c100-2dd8-11eb-8ae4-0b4d1ad425a3.PNG)

`Git Commits`

![깃 커밋](https://user-images.githubusercontent.com/71081825/99965255-f2396b80-2dd7-11eb-89e0-a0f1b4b97628.PNG)

 `class 구성정보 및 주요 코드`
![클래스 구성 정보 및 주요 코드](https://user-images.githubusercontent.com/71081825/99965389-24e36400-2dd8-11eb-804f-233bedcde2b4.PNG)



최종 프로젝트 발표

A , D 버튼을 이용한 플레이어 좌우 이동

SPACEBAR 버튼을 이용한 플레이어 점프 구현 - 2회 (더블점프) 가능

LSHIFT 버튼을 이용한 쉴드 생성 - 몬스터 공격 방어

-쉴드 게이지 존재 쉴드 미사용시 게이지 충전, 사용시 소진

MOUSEBUTTON_DOWN 이벤트를 이용한 플레이어의 공격

 -쉴드로 공격 방어 한뒤 1초가 지나기 전에 마우스 클릭시 마우스 좌표로 공격 (반격)

몬스터

-PLANT  플레이어 좌표로 공격, 가까울수록 느리게 멀수록 빠른 공격을 한다 

-TREE   플레이어 좌표로 공격, 균일한 속도로 공격을한다.

-PIG_BOMB  플레이어 좌표로 공격, 포물선 운동을하며 플레이어 근처에 떨어진다 (3STAGE부터 출현)

* 주차별 진척도![최종 주차 별 진척도](https://user-images.githubusercontent.com/71081825/101364645-2471bf80-38e6-11eb-8e6f-b13b43a1c3e1.PNG)

* 깃 커밋 최종![최종 깃](https://user-images.githubusercontent.com/71081825/101364692-318eae80-38e6-11eb-9c03-1a63b3037ec0.PNG)

* 로고 화면![로고화면](https://user-images.githubusercontent.com/71081825/101364390-dceb3380-38e5-11eb-9796-1447b18295b0.png)

* 메인 화면![메인화면](https://user-images.githubusercontent.com/71081825/101364396-deb4f700-38e5-11eb-908d-0b7125040055.png)

* 플레이 화면![플레이화면1](https://user-images.githubusercontent.com/71081825/101364408-e1175100-38e5-11eb-95bb-ff8ac3f49024.png)

  ![플레이화면2](https://user-images.githubusercontent.com/71081825/101364409-e2487e00-38e5-11eb-81f9-1d5a53d47243.PNG)

* 랭킹화면![랭킹화면](https://user-images.githubusercontent.com/71081825/101364586-1623a380-38e6-11eb-9547-25ebbf93be75.png)

발표 영상 링크 및 Setup 파일링크

1차 발표

https://www.youtube.com/watch?v=LldBgOkUuaM

2차 발표

https://www.youtube.com/watch?v=2q2LX_ZLDHo

최종 발표

https://www.youtube.com/watch?v=Ec0mj2oeljs

Setup.exe

https://drive.google.com/file/d/1Ca_V4nruqQFfnkzlrT8c1ZTAX54RJERB/view?usp=sharing