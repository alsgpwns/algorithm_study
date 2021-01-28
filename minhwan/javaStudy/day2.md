
# 나누어 떨어지는 배열
1. https://programmers.co.kr/learn/courses/30/lessons/12910

import java.util.*;

```
class Solution{
    public int[] solution(int[] arr, int divisor) {
   

        
        int result[] = Arrays.stream(arr).filter(index -> index % divisor ==0).toArray();
        //result 배열의 인덱스를  0으로 나누었을 때 나머지가 0 인 인덱스 추출            
      
        Arrays.sort(result);
    	//오름차순 정렬

        if(result.length ==0) {
            result = new int[1];
            result[0] = -1;
        }
	// 나누어 떨어지는 값이 없을경우 배열에 -1담아 리턴
	
        System.out.println(Arrays.toString(result));
     return result;
    }
   
}
```

# 문자열 내마음대로 정렬하기 
2. https://programmers.co.kr/learn/courses/30/lessons/12915
```
import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
             Arrays.sort(strings, new Comparator<>() {
            // 오름차순 정렬  Comparator 생성 후 compare 메서드 적용
        @Override
            public int compare(String a,String b) {
                if(a.charAt(n) > b.charAt(n))
                    return 1;
                else if(a.charAt(n) == b.charAt(n))
                    return a.compareTo(b);
                else 
                    return -1;
            }
        });
        /*
        첫 번째 파라미터로 넘어온 객체 > 두 번째 파라미터로 넘어온 객체: 1 리턴
        첫 번째 파라미터로 넘어온 객체 == 두 번째 파라미터로 넘어온 객체: 0 리턴
        첫 번째 파라미터로 넘어온 객체 < 두 번째 파라미터로 넘어온 객체: -1 리턴
        */
        // 비교 후 , 배열 리턴
        return strings;
    }
}
```



# 문자열 내림차순으로 배치하기 
3. https://programmers.co.kr/learn/courses/30/lessons/12917

```
import java.util.Arrays;

class Solution {
    public String solution(String s) {
        char[] c = s.toCharArray();
        Arrays.sort(c);
        //배열에 담아 오름차순 정렬
        String result = new String(c);
        return new StringBuffer(result).reverse().toString();
    //데이터들을 역순으로 처리 
    }
}
```