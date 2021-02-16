# Day8 [Level1]
### 문제1
![image](https://user-images.githubusercontent.com/45223821/106562713-0f27b300-656e-11eb-822c-4efe8e4c03ed.png)


<https://programmers.co.kr/learn/courses/30/lessons/12944>
### 문제 설명
int형 배열의 값을 double형으로 평균을 내어 return한다.

### 풀이
```java
class Solution {
    public double solution(int[] arr) {
        double answer = 0;
            for(int i = 0; i < arr.length; i++)
            {
                answer += (arr[i]);
            }
            answer = answer/arr.length; 
            return answer;
    }
}
```
### 다른 풀이
- Stream을 이용한 풀이
 ```java
public class Solution  {
        public double solution(int[] arr) {
            return (int) Arrays.stream(array).average().orElse(0);
        }
}
```



---
### 문제2
![image](https://user-images.githubusercontent.com/45223821/106562941-675eb500-656e-11eb-8ff7-de47805b8f35.png)


<https://programmers.co.kr/learn/courses/30/lessons/12925>

### 문제 설명
문자열 s를 정수형으로 return한다.


### 풀이
형변환 메소드를 사용했다.
```java
class Solution {
  public int solution(String s) {
      int answer = 0;
      answer = Integer.parseInt(s);
      return answer;
  }
}

```
### 다른 풀이
```java
 조건문? 참일때 : 거짓일 때 // 삼항연산자
```
1. 부등호를 판단할 sign변수를 true로 초기화한다.

2. 변수ch에 문자열s의 한글자씩을 담는다.

3. ch가 -라면, sign 변수에 false를 대입

4. ch가 +가 아니라면, result * 10 + (ch-'0')을 해준다.

    - 부등호 '+'없이 반환해야되기 때문

5. 삼항 연산자를 이용해 return한다.

    - sign이 true일 때 result를 return

    - sign이 false일 때 result*-1을 return

```java
class Solution {
	public int solution(String s) {
        /*첫번째*/
		boolean sign= true;
		int result = 0;

        /*두번째*/
		for (int i = 0; i < s.length(); i++) {
			char ch = s.charAt(i);
            /*세번째*/
			if (ch == '-')
				sign = false;
			else if(ch !='+')
				result = result * 10 + (ch - '0');
		}
        /*네번째*/
		return sign? result:-1 * result;
	}
}

```


---
### 문제3
![image](https://user-images.githubusercontent.com/45223821/106564027-033cf080-6570-11eb-98df-36cbfdd663f1.png)



<https://programmers.co.kr/learn/courses/30/lessons/42576>

### 문제 설명
participant배열에서 completion 배열에 없는 문자열을 return한다.


### 풀이
(문제를 읽다보니, participant가 completion보다 항상 1이 크다는것을 알게되었다. 이것을 이용해서 풀었다.)

1. participant배열을 hashMap에 넣고, completion으로 검색한다.

2. 검색했을 때 value가 0보다 크다면 value -1을, value가 0보다 작다면 remove를 해준다.

3. 결국 hashMap엔 완주 하지 못한 한명의 선수만 남게되고, return 해준다.
```java
import java.util.HashMap;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer="";
	int value=0;
	HashMap<String, Integer>hm = new HashMap<String, Integer>();

		//넣기
		for(String p:participant)
		{
			if(hm.get(p)==null)
			{
				hm.put(p, 1);
			}
			else {
				hm.put(p, hm.get(p)+1);
			}
		}
        
        //검색
		for(String c:completion) {
			if(hm.get(c)>0) {
				hm.replace(c, hm.get(c)-1);
			}
			if(hm.get(c)<=0){
				hm.remove(c);
			}	
		}
		
        for(String key : hm.keySet()) answer=key;
        return answer;
    }
}
```

### 삽질
처음에 생각했던 알고리즘이다.
key에 더미 값을 넣고, value에 선수 이름을 넣었다.
value를 이용해 key 값을 찾아야 했었고, 이를 위해 같은 메소드를 이용했다.
- 정확성 50점 / 효율성 0점
  
```java
	public Object getKey(HashMap<Integer, String> m, String value) {

		for(Object o: m.keySet()) {

	        if(m.get(o).equals(value)) {
	            return  o;
	        }
	    }
	    return null;
	}
```

### 다른 풀이
- 찾는 키가 존재하면 해당키의 값을 반환하고, 없으면 기본값을 반환한다.
```java
getOrDefault
```


- 위의 문제에서는 아래와 같이 적용할 수 있다.
  - map.put(a, (a의 값이 존재하면 a의 값을 넣어주고 없다면 0)+1)
```java
for(String a: arr1)
hm.put(a, map.getOrDefault(a,0)+1);
```


---

# [In progress]

### 문제4 [In progress]
유형 : 완전 탐색

문제명 : 모의고사

<https://programmers.co.kr/learn/courses/30/lessons/42840>


### 문제 설명
- 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
- 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
- 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

### 입출력 예
![image](https://user-images.githubusercontent.com/45223821/106563288-e9e77480-656e-11eb-950b-13be29bd0032.png)

입출력 예 #1

- 수포자 1은 모든 문제를 맞혔습니다.
- 수포자 2는 모든 문제를 틀렸습니다.
- 수포자 3은 모든 문제를 틀렸습니다.
따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.


### 풀이
1. 수포자 1, 2, 3 비교하기 위해 각각 10개의 Index로 초기화 한다.
2. answersheet를 10개의 Index로 초기화 한다.
   - 수포자와 answewrsheet를 비교하기 위함
3. 수포자와 answersheet를 비교해, 정답이 맞다면 +1해준다. 
   - 체점
4. 배열의 maxIndex, minIndex, middle을 구한다.
   - 1등 2등 3등을 구해줌
5. 0점이 아니라면, arrayList에 add해준다.
```java
import java.util.ArrayList;
class Solution {
    public ArrayList<Integer> solution(int[] answers) {
        int[] answer = new int[3];
        ArrayList <Integer> arrList = new ArrayList<Integer>();
        /*첫번째*/
	int[] 수포자1= {1,2,3,4,5,1,2,3,4,5};
	int[] 수포자2= {2,1,2,3,2,4,2,5,2,1};
	int[] 수포자3= {3,3,1,1,2,2,4,4,5,5};
        
        /*두번째*/
	int[] anwersheet = new int[10];
        System.arraycopy(answers, 0, anwersheet, 0, answers.length);
	System.arraycopy(answers, 0, anwersheet, 5, answers.length);
        
        /*세번째*/
        for(int i=0; i<5; i++) {
		if(anwersheet[i]==수포자1[i]) answer[0]+=1;
		else if(anwersheet[i]==수포자2[i]) answer[1]+=1;
		else if(anwersheet[i]==수포자3[i]) answer[2]+=1;
	}
		
        /*네번째*/
	int minIndex=0;
	int maxIndex=1;
	int middle=2;
	for(int i=0; i<answer.length; i++) {
		if(answer[minIndex]>answer[i]) minIndex=i+1;
		else if(answer[maxIndex]<answer[i]) maxIndex=i+1;
		else middle =i+1;
	}

        /*다섯번째*/
	if(answer[0]!=0) arrList.add(maxIndex);
	if(answer[1]!=0) arrList.add(middle);
	if(answer[2]!=0) arrList.add(minIndex);
        
        return arrList;
    }
}
```

---
### 문제5 [In progress]
유형 : 연습문제

문제 명 : 이상한 문자 만들기

<https://programmers.co.kr/learn/courses/30/lessons/12930>

### 문제 설명
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

- 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다. 
- 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다


### 입출력 예
![image](https://user-images.githubusercontent.com/45223821/106563523-3b8fff00-656f-11eb-8a49-f52ca199fc1f.png)
  - try hello world는 세 단어 try, hello, world로 구성되어 있습니다. 각 단어의 짝수번째 문자를 대문자로, 홀수번째 문자를 소문자로 바꾸면 TrY, HeLlO, WoRlD입니다. 따라서 TrY HeLlO WoRlD 를 리턴합니다.


### 풀이
- 생각한 알고리즘 
![image](https://user-images.githubusercontent.com/45223821/106566097-2f0da580-6573-11eb-9cf0-f896b1354b95.png)

1. 문자 " "을 기준으로 문자열을 자른후, 배열에 넣는다.
   - split이용
2. 배열을 모두 소문자로 바꾸어준다.
3. 이중 for문
   - 배열의 i번째 방의 j번째 문자중, 짝수번째 문자를 대문자로 바꾸어줌
   - 배열의 i번째 방의 j번째 문자중, 홀수번째 문자를 대문자로 바꾸어줌
4. 배열의 마지막 방이 아니라면, 띄어쓰기 해줌


[ex]
1. 원래 문자열
HI this Is Hye

2. split 이용
[HI, this, Is, Hye]

3. toLowerCase 이용
[hi, this, is, hye]

4. 이중 for문
Hi ThIs Is HyE

```java
class Solution {
    public String solution(String s) {
        String answer = "";
        String temp="";
        /*첫번째*/
        String[] arr=s.split(" ");
        /*두번째*/
        s.toLowerCase();        
        
        /*세번째*/
        for(int i=0; i<arr.length; i++) {
        	for(int j=0; j<arr[i].length(); j++) {
        		if(j%2==0) {
        			temp = arr[i].charAt(j)+"";
        			answer+=temp.toUpperCase();
        		}else {
        			answer +=arr[i].charAt(j);
        		}        		
        	}
            /*네번째*/
        	if(!(i==arr.length-1)) answer+=" ";
        }
        
        return answer;
    }
}
```
