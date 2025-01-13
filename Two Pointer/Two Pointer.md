## 📚 Two Poiner
#### 개념
📌 투 포인터 알고리즘이란?
> 투 포인터 알고리즘은 리스트에 순차적으로 접근해야 할 때 두개의 점의 위치를 기록하면서 처리하는 알고리즘을 의미한다.<br>
> 리스트에 담긴 데이터에 순차적으로 접근해야 할 때는 시작점과 끝점 2개의 점으로 접근할 데이터의 범위를 표현할 수 있다.

<br><br>
#### 대표 문제 : <mark>특정한 합을 가지는 부분 연속 수열 찾기</mark>
📌 문제 설명
> N개의 자연수로 구성된 수열이 있다.<br>
> **합이 M인 부분 연속 수열의 개수**를 구하는 문제<br>
> 수행 시간 제한은 O(N)
<br>

📌 주어진 수열, M

> 수열 : [1, 2, 3, 4, 5] <br>
> M=5

<br>

📌 접근 방법

① 초기화
> 두 개의 포인터 `start`와 `end`를 0번 인덱스로 초기화<br>
> 현재 부분 수열의 합을 나타낼 변수 `current_sum`을 0으로 설정

② 포인터 이동 및 합 계산
> `current_sum`이 **M보다 작은 경우**: `end`를 오른쪽으로 한 칸 이동하고, `current_sum`에 `수열[end]` 값을 더함.<br>
> `current_sum`이 **M보다 큰 경우**: `start`를 오른쪽으로 한 칸 이동하고, `current_sum`에서 `수열[start]` 값을 뺌.<br>
> `current_sum`이 **M과 같은 경우**: 부분 수열의 개수를 증가시키고, `end`를 오른쪽으로 이동한 뒤 위 과정을 반복.

③ 종료 조건
> `end`가 수열의 끝까지 도달하면 알고리즘 종료

④ 시간 복잡도
> `start`와 `end`포인터는 각각 리스트의 끝까지 최대 한번씩 이동하므로 시간 복잡도는 **O(N)**

<br><br>

#### 내가 푼문제
[📌 BJ11728](https://www.acmicpc.net/problem/11728)<br>
[📌 BJ2003](https://www.acmicpc.net/problem/2003)<br>
[📌 BJ3273](https://www.acmicpc.net/problem/3273)<br>
[📌 BJ12891](https://www.acmicpc.net/problem/12891)<br>
[📌 BJ2531](https://www.acmicpc.net/problem/2531)<br>
[📌 BJ1806](https://www.acmicpc.net/problem/1806)
