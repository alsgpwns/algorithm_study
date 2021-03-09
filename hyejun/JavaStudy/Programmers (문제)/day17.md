# Day17 [완전탐색/시뮬레이션]
## 문제
![image](https://user-images.githubusercontent.com/45223821/110488541-ea58c980-8131-11eb-9c18-7e24f647f87a.png)


<https://programmers.co.kr/learn/courses/30/lessons/67257>

## 문제 설명
연산자에 우선순위를 정해, 우선순위대로 모든 경우의 수를 연산한다.

연산 결과의 절대값이 가장 큰 수를 return한다.
![image](https://user-images.githubusercontent.com/45223821/110488549-ec228d00-8131-11eb-997b-205748a3f37e.png)

## Ref
1. 순열 구현 https://swycha.tistory.com/133

2. [method] list add(int index, E element) method https://www.geeksforgeeks.org/list-addint-index-e-element-method-in-java/

3. [method] list clone https://codechacha.com/ko/java-collections-arraylist-clone/

4. [error] java.lang.Long cannot be cast to java.lang.Integer https://wwwnghks.tistory.com/123
   

## 풀이
코드가 지저분하고 구현이 복잡해서 그렇지 알고리즘은 간단하다.

1. 연산자를 저장

2. 피연산자를 저장

3. 계산

​

- 상세한 알고리즘 설명

1. 연산자를 저장

    1-1. 연산자의 모든 경우의수를 저장

2. 피연산자 저장

3. 계산

    3-1. 1번에서 저장한 연산자의 우선순위와 expression의 연산자를 비교해 같다면, 계산 수행

    3-2. 연산자의 양옆 index인 피연사자를 가지고 계산한다.

    3-3. 계산 후 결과값을 가지고, 직전 계산식에 결과를 삽입한다.

    3-4. 결과값에 절대값을 씌워, 결과를 비교한 후, 가장 큰 결과를 answer에 삽입

```java
import java.util.*;
class Solution {
    public long solution(String expression) {
        long answer = 0;
        Solution sol = new Solution();
		ArrayList<Long> oper = new ArrayList<Long>();
		ArrayList<Integer> operand_list = new ArrayList <Integer>();
		ArrayList<Integer> operandSet = new ArrayList <Integer>(); // 
		HashSet<Integer> operand = new HashSet<Integer>();
        
        // 1. 연산자	
		// 연산자+피연산자 저장
		StringBuilder temp= new StringBuilder("");
		for(int i=0; i<expression.length(); i++) {
			char sign = expression.charAt(i);
			
			if( sign=='-'||sign=='*'||sign=='+') {
				oper.add((long) (Integer.parseInt(temp.toString())));
				temp.delete(0, temp.length());
				if( sign=='-') {
					operand.add(2);
					operand_list.add(2);
				} else if(sign=='*'){
					operand.add(3);
					operand_list.add(3);
				} else if(sign=='+'){
					operand.add(1);
					operand_list.add(1);
				}
			}
			
			if(sign>='0' && sign<='9') temp.append(sign);
			if(i==expression.length()-1) oper.add((long) (Integer.parseInt(temp.toString())));
		}
        
        Iterator it = operand.iterator();
		int count=0;
		int[] arr = new int[operand.size()];
		while(it.hasNext()) {
			arr[count++]=(int) it.next();
		}
        
        sol.doPermutation(arr, 0, operandSet); // 연산자 모든 경우의수 구하기
        
        // 2. 계산
		long result =0;
		long min=0;
		for(int i=0; i<operandSet.size(); i++) {
			ArrayList<Long> copy_oper = (ArrayList<Long>) oper.clone(); // 피연산자
			ArrayList<Integer> copy_operand = (ArrayList<Integer>) operand_list.clone(); //연산자
			
			for(int j=0; j<oper.size(); j++) {
				int priority = operandSet.get(i); //우선순위
				int sign = copy_operand.get(j); // 연산자
				
                // 3-2. 계산 호출
				if(sign == priority) {
					if(j==oper.size()) {
						long num1 = copy_oper.get(j-1);
						long num2 = copy_oper.get(j);
						result = calc(sign,num1,num2);
					} else {						
						long num1 = copy_oper.get(j);
						long num2 = copy_oper.get(j+1);
						result = calc(sign,num1,num2);
					}
					
					// 3-3. 계산식 삽입, 계산을 완료한 연산자와 피연산자 삭제
					copy_oper.remove(j);
					copy_oper.remove(j);
					copy_operand.remove(j);
					copy_oper.add(j,result);
					
					// 3-4. 결과값 대소 비교 (answer에 대입)
					if(copy_operand.size()!=0) j=-1; // 식의 모든 계산이 완료되지 않았다면 for문을 다시 돈다
					else {
						min = Math.abs(result);
						if(min>answer) answer=min;
						break;
					}
				}
				
                 // 식의 모든 연산자를 계산하기 위함 (-라면 -연산을 한번만 하지 않게)
				for(int k=0; k<copy_operand.size(); k++) { 
					if(!copy_operand.contains(priority)) {
						i++;
						break;
					}
					else break;
				}
			}
			
		}
        return answer;
    }
    
    // 순열 구하기
	public void doPermutation(int[] arr, int startIdx, ArrayList<Integer> operandSet) {
		int length = arr.length;

		if(startIdx == length - 1) {
			for(Integer n:arr) {
				operandSet.add(n);				
			}
			return;
		}
		for(int i = startIdx; i < length; i++) {
			swap(arr, startIdx, i);
			doPermutation(arr, startIdx + 1, operandSet);
			swap(arr, startIdx, i);
		}
	}

	public void swap(int[] arr, int n1, int n2) {
		int temp = arr[n1];
		arr[n1] = arr[n2];
		arr[n2] = temp;
	}
	
	
	// 계산하기
	public long calc(int oper, long num1, long num2) {
		long result = 0;
		switch(oper) {
		case 1 : //+
			return num1+num2;
		case 2 : //-
			return num1-num2;
		case 3 : //*
			return num1*num2;
		}
		return result;
	}
}
```


## 다른 풀이
dfs 사용 풀이 

출처: https://hidelookit.tistory.com/69

1. 완전 탐색을 사용해 수식의 모든 조합을 구한다.

2. 기존 수식 중 조합의 순서와 맞는 수식을 발견하면 앞뒤 숫자와 수식으로 계산한 후 다시 리스트에 넣어준다.

3. 2번을 반복한 후 더 큰 값을 비교한다.
   
```java
import java.util.*;

class Solution {
    
    private static char[] cal = {'+', '-', '*'}; //조합에 사용
    private static char[] temp = new char[3]; //모든 조합
    private static boolean[] visit = new boolean[3]; //방문 체크
    private static ArrayList<Long> nums = new ArrayList<Long>(); //주어진 숫자 담기
	private static ArrayList<Character> ops = new ArrayList<Character>(); //주어진 문자 담기
    private static long answer; //답
    
    public long solution(String expression) {
        answer = 0;
        
        String num = "";
        for (int i=0; i<expression.length(); i++) {
            if (expression.charAt(i) >= '0' && expression.charAt(i) <= '9') {
                num += expression.charAt(i);
            } else {
                nums.add(Long.parseLong(num));
                num = "";
                ops.add(expression.charAt(i));
            }
        }
        //마지막 숫자
        nums.add(Long.parseLong(num));
        
        dfs(0);
        
        return answer;
    }
    
    public void dfs(int start) {
        
        if (start == 3) {
            // + - * 
            // + * - 
            // - + * 
            // - * + 
            // * + - 
            // * - + 
            
            math();
            
        } else {
            
            for (int i=0; i<3; i++) {
                if (!visit[i]) {
                    visit[i] = true;
                    temp[start] = cal[i];
                    dfs(start+1);
                    visit[i] = false;
                }
            }
            
        }
        
    }
    
    public void math() {
        // 주어진 숫자와 연산 그대로 복사
    	ArrayList<Long> copyNums = new ArrayList<>(nums);
    	ArrayList<Character> copyOps = new ArrayList<Character>(ops);
        
        for (int i=0; i<temp.length; i++) {
            for (int j=0; j<copyOps.size(); j++) {
                if (temp[i] == copyOps.get(j)) {
                    //숫자2개, 연산자1개 보내서 연산
                    Long res = calc(copyNums.remove(j), copyNums.remove(j), temp[i]);
                    //연산결과값 넣기
                    copyNums.add(j, res);
                    copyOps.remove(j);
                    j--;
                }
            }
        }
        answer = Math.max(answer, Math.abs(copyNums.get(0)));
        
    }
    
    public static Long calc(Long num1, Long num2, char op) {
    	switch (op) {
			case '+': {
				return num1 + num2;
			}
			case '-': {
				return num1 - num2;
			}
			case '*': {
				return num1 * num2;
			}
    	}
    	return (long)0;
    }
    
}
```

## 삽질
1. 범위 초과

    이 문제는 int형으로 연산했을 때 범위 초과 에러가 난다.

    그래서 long형으로 변환시켜주었지만, test case 3개에서 런타임 오류가 났다.

    문제는 아래의 부분이었는데, String→Integer→long형으로 변환하는 과정에서 범위를 초과에러가 뜬것같다.

    (test case를 작게 넣어주면 에러가 나지 않는데, 일정 범위 이상 넘어가면 에러가 남)

    이후에 모든 부분을 long형으로 바꾸어주니, 잘 돌아갔다.

    ```java
    long num1 = Integer.parseInt(String.valueOf(copy_oper.get(j)));
    long num2 = Integer.parseInt(String.valueOf(copy_oper.get(j+1)));

    java.lang.NumberFormatException: For input string: "66000000000" //에러 메세지
    ```

2. String 이용하기
   처음 생각한 방법은 list를 쓰지 않고, String을 이용해 바로 사용하는 법이었다.

    이 방법을 이용해 짜봤지만, 아래와같은 이유로 포기했다.

   1. int형은 +,-가 구분되지만, String은 +,-구분이 어렵다는 점 (-부등호를 가지고 있었는지 or 결과값이 - 인지 확인이 어려움)

   2. 계산을 수행한 후, 결과를 넣어주는 과정에서 index를 찾기 어려웠다.


    ```java
     // 2. 계산
		StringBuilder num1 = new StringBuilder("");
		String num2="";
		int start=0;
		int end = 0;
		long min=0;
		int n=0;
		StringBuilder exp = new StringBuilder(expression);
		
		for(int i=0; i<list.size(); i++) {
			if(i%hs.size()==0) 
				exp = new StringBuilder(expression);
			String oper = list.get(i);
			for(int j=0; j<exp.length(); j++) {
				String text = exp.charAt(j)+"";
				
				if(exp.charAt(j)>=48 && exp.charAt(j)<=57) {
					num1.append(exp.charAt(j));
				} else {
					if(oper.contentEquals(text)) {
						start = j - num1.length(); //
						num2=num1.toString();
						num1.delete(0, num1.length());
					}else {
						num1.delete(0, num1.length());
					}
				}

				if(!num2.isEmpty() && num1.length()!=0) {
					long temp1 = Integer.parseInt(num1.toString());
					long temp2 = Integer.parseInt(num2);
					int len = num1.length()+num2.length(); 
					
					if(start<0) start=0;
					
					// 수식 호출
					min = Math.abs( 수식.calc(oper, temp1, temp2) );
					
					// 계산식 교체
					exp.delete(start, j+1);
					exp.insert(start, min);
					
					// 초기화
					num1.delete(0, num1.length());
					num2="";
					if( (i+1) % hs.size()==0) j=-1;
				} // if 종료
	
			} //안쪽 for문 종료 
			if( (i+1) % hs.size()==0) {
				answer = min; 
			}
		}
		
		
		return answer;
	}
    ```