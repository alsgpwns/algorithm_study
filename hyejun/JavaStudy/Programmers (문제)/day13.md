# Day13 [Level3/hash]
### 문제
![image](https://user-images.githubusercontent.com/45223821/108545411-19e29600-732b-11eb-920d-125930623485.png)

<https://programmers.co.kr/learn/courses/30/parts/12077>


### 문제 이해
1. 문제

    스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

    1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.

    2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.

    3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

    노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
    ![image](https://user-images.githubusercontent.com/45223821/108545418-1c44f000-732b-11eb-82f6-a93bb5e6d9d1.png)

2. 이해

    (장르들이 저장되는 genres 배열, 플레이 횟수가 저장되는 plays 배열을) 매개변수로 받아 장르별로 플레이 횟수를 합산한다.

    1. 가장 많이 재생된 장르

    2. 장르에서 가장 많이 재생된 인덱스 2개를 return

    ​

    여기서 헷갈렸던 부분이 2번 (장르에서 가장 많이 재생된 인덱스 2개를 return 하는 부분)이었다.

    문제와 제한사항을 꼼꼼하게 읽어봐야겠다.

### 풀이
1. 이중 해시맵을 사용해  {장르 {index, play횟수}} 형태로 저장
    - Key중복 저장이 안되기 때문에, inner map key를 index 값으로 저장함
2. 해시맵을 이용해 {장르 , 총 play 횟수} 형태로 저장
3. 2번에서 저장한 해시맵을 Key만 저장한 배열로 만든 후, 배열을 내림차순으로 정렬
4. 장르당 2개씩 베스트 앨범을 뽑아 answer_list에 저장
```java
import java.util.*;
import java.util.Map.Entry;

class Solution {
    public ArrayList<Integer>  solution(String[] genres, int[] plays) {
       HashMap<String, HashMap<Integer,Integer>> map = new HashMap<String, HashMap<Integer, Integer>>();
		HashMap<String, Integer> sumMap = new HashMap<String,Integer>();
		ArrayList<Integer> answer_list =new ArrayList<Integer>(); 

		// 1. map에 genres, plays 삽입
		for(int i=0; i<genres.length; i++) {
			if(!map.containsKey(genres[i])) {
				map.put(genres[i], new HashMap<Integer,Integer>());
				map.get(genres[i]).put(i, plays[i]);
			} 
			else {
				HashMap<Integer, Integer> inner= map.get(genres[i]);
				map.put(genres[i],inner);
				inner.put(i, plays[i]);
			}
		}			
        
        // 2. set생성
		int temp=0;
		String genre_set[] = new String[map.size()];
		for (String key : map.keySet()) {
			genre_set[temp++]=key;
		}
        
        // 3. 총합을 담을 hashmap 만듬
       for(int i=0; i<map.size(); i++ ) {
			HashMap<Integer, Integer> entry = map.get(genre_set[i]);
			for(Integer value : entry.values()) {
				if(!sumMap.containsKey(genre_set[i]))
					sumMap.put(genre_set[i], value);
				else {
					int pre_value = sumMap.get(genre_set[i]);
					sumMap.put(genre_set[i], pre_value+value);
				}
			}
		}
        
        // 4. 해시맵을 value로 정렬
		List<Entry<String, Integer>> sum_list = new ArrayList<Entry<String, Integer>>(sumMap.entrySet());

		// 비교함수 Comparator를 사용하여 내림 차순으로 정렬
		Collections.sort(sum_list, new Comparator<Entry<String, Integer>>() {
			// compare로 값을 비교
			public int compare(Entry<String, Integer> obj1, Entry<String, Integer> obj2)
			{
				// 내림 차순으로 정렬
				return obj2.getValue().compareTo(obj1.getValue());
			}
		});

        
        // 5. 4번을 key만 저장
        temp=0;
		String sumArr[] = new String[sum_list.size()];
		for (int i=0; i<sum_list.size(); i++) {
			Entry<String, Integer> sum_entry=sum_list.get(i);
			String key = sum_entry.getKey();
			sumArr[temp++]=key;
		}

        // 6. 각각 내림차순으로 정렬하면서 answer에 저장
        int count=0;
		for(int i=0; i<genre_set.length; i++) {
			List<Entry<Integer, Integer>> list_map = new ArrayList<Entry<Integer, Integer>>(map.get(sumArr[i]).entrySet());
			Collections.sort(list_map, new Comparator<Entry<Integer, Integer>>() {
				public int compare(Entry<Integer, Integer> obj1, Entry<Integer, Integer> obj2)
				{
					return obj2.getValue().compareTo(obj1.getValue());
				}
			});
            // 6-1. answer에 저장 
			for(Entry<Integer, Integer> entry : list_map) {
				count++;
                if(list_map.size()==1) {
					answer_list.add(entry.getKey());
                    count=0;
					break;
				}
				if(count<=2) answer_list.add(entry.getKey());
				if(count>=2){
					count=0;
					break;
				}

			}
		}
        
        return answer_list;
    }
}
```

### 자세한 풀이
```java
// 입력 예시
String genres[]= {"A", "B", "A", "B", "A", "C"};
int plays[] = {500, 600, 150, 800, 2500, 5000};
```

1. 중첩 hashmap을 이용해 genres, plays 삽입

    - <String, <Integer, Integer>> 형식으로 삽입된다.

    - hashmap은 key의 중복을 허용하지 않기 떄문에, 
      - if 구절에서 최초 삽입을 해주고, 
      - else 구절에서 map.get으로 innerHashmap을 가져온 후, 넣어줄 값과 함께 삽입한다.

    ```java
    HashMap<String, HashMap<Integer,Integer>> map = new HashMap<String, HashMap<Integer, Integer>>();

		// 1. map에 genres, plays 삽입
		for(int i=0; i<genres.length; i++) {
			if(!map.containsKey(genres[i])) {
				map.put(genres[i], new HashMap<Integer,Integer>());
				map.get(genres[i]).put(i, plays[i]);
			} 
			else {
				HashMap<Integer, Integer> inner= map.get(genres[i]);
				map.put(genres[i],inner);
				inner.put(i, plays[i]);
			}
		}	

    ```
    ```java
    // System.out.println(map);
    {A={0=500, 2=150, 4=2500}, B={1=600, 3=800}, C={5=5000}}
    ```


2. keySet을 저장

    - KeySet을 배열에 저장해준다.

    - 3번에서 (총 합을 담을)hashmap을 보다 쉽게 만들기 위함 → 분명 다른 방법이 있겠지만, 나는 배열이 더 접근하기 수월해서 배열로 저장했다.
    ```java
    // 2. set생성
	int temp=0;
	String genre_set[] = new String[map.size()];
	for (String key : map.keySet()) {
		genre_set[temp++]=key;
	}
    ```
    ```java
    // System.out.println(Arrays.toString(genre_set));
    [A, B, C]
    ```

3. 총 합을 담을 hashmap을 만듦

   - 1번과 hashmap을 만드는 방법은 같다.

   - 총 합을 계산해 주어야 하기 때문에 여기서 중요한 점은, 기존 map에 있던 entry를 get으로 받아와서, 넣어줄 값과 함께 합해서 넣어준다.

    ```java
    // 3. 총합을 담을 hashmap 만듬
            for(int i=0; i<map.size(); i++ ) {
                HashMap<Integer, Integer> entry = map.get(genre_set[i]);
                for(Integer value : entry.values()) {
                    if(!sumMap.containsKey(genre_set[i]))
                        sumMap.put(genre_set[i], value);
                    else {
                        int pre_value = sumMap.get(genre_set[i]);
                        sumMap.put(genre_set[i], pre_value+value);
                    }
                }
            }
    ```
    ```java
    // System.out.println(sumMap);
    sumMap: {A=3150, B=1400, C=5000}
    ```


4. 해시맵(sumMap)을 value로 내림차순 정렬

    hashmap을 내림차순 하기 위해 list를 이용한다.

    ```java
    // 4. 해시맵(sumhash)을 value로 내림차순 정렬
		List<Entry<String, Integer>> sum_list = new ArrayList<Entry<String, Integer>>(sumMap.entrySet());

		// 비교함수 Comparator를 사용하여 내림 차순으로 정렬
		Collections.sort(sum_list, new Comparator<Entry<String, Integer>>() {
			// compare로 값을 비교
			public int compare(Entry<String, Integer> obj1, Entry<String, Integer> obj2)
			{
				// 내림 차순으로 정렬
				return obj2.getValue().compareTo(obj1.getValue());
			}
		});
    ```
    ```java
    // System.out.println(sum_list);
    [C=5000, A=3150, B=1400]
    ```
5.  4번을 key만 저장

- 내림차순 정렬된 hashmap의 key만 배열에 저장한다. (정확히 말하면 hashmap을 list로 받아와 내림차순 한 후, key만 배열에 저장)
    ```java
    temp=0;
	String sumArr[] = new String[sum_list.size()];
	for (int i=0; i<sum_list.size(); i++) {
		Entry<String, Integer> sum_entry=sum_list.get(i);
		String key = sum_entry.getKey();
		sumArr[temp++]=key;
	}
    ```
    ```java
    // System.out.println(Arrays.toString(sumArr));
    [C, A, B]
    ```

6.  각 장르를 내림차순으로 정렬하면서 answer에 대입

    - 4번에서 사용한 방법과 같은 방법으로 내림차순 정렬한다.

    - (다른 방법이 있겠지만,) hashmap은 list로 정렬하는게 편해서 아래와 같은 방법을 사용했다.

    - 여기서 중요한 점은 아래와 같이, 장르 하나씩만을 list로 받아올 수 있다는 점이다.
        ```java
        A={0=500, 2=150, 4=2500} // map.get(sumArr[0]).entrySet()
        B={1=600, 3=800} // map.get(sumArr[1]).entrySet()
        C={5=5000} // map.get(sumArr[2]).entrySet()
        ```
    - 위와 같은 이유로, 이중 for문을 사용해 answer list에 대입한다. 

        - ( 여기서 answer를 배열로 쓰지 않은 이유는, answer 배열의 크기를 구하지 않기 위해서 )

    - 밖 for문에서 map의 entry로 받아온 list_map을 내림차순으로 정렬하고, 안 for문에서 answer_list에 대입한다.

    - 안쪽 for문에서 대입할 때, 중요한 점은 장르 당 play횟수가 높은 두 곡만 넣어준다는 것이다. (그래서 조건문이 길어짐)

    - 이것 때문에 시간 엄청 잡아먹음

    ```java
    int count=0;
        // 6. ﻿각 장르를 내림차순으로 정렬하면서 answer에 대입
		for(int i=0; i<genre_set.length; i++) {
			List<Entry<Integer, Integer>> list_map = new ArrayList<Entry<Integer, Integer>>(map.get(sumArr[i]).entrySet());
			Collections.sort(list_map, new Comparator<Entry<Integer, Integer>>() {
				public int compare(Entry<Integer, Integer> obj1, Entry<Integer, Integer> obj2)
				{
					return obj2.getValue().compareTo(obj1.getValue());
				}
			});
            
            // 6-1. answer list에 대입
			for(Entry<Integer, Integer> entry : list_map) {
				if(list_map.size()==1) {
					answer_list.add(entry.getKey());
					break;
				}
				count++;
				if(count<=2) answer_list.add(entry.getKey());
				if(count>=2){
					count=0;
					break;
				}

			}
		}
    ```
    ```java
    // System.out.println(answer_list);
    [5, 4, 0, 3, 1]
    ```
### 다른 풀이
nested hashmap을 사용하지 않은 풀이
```java
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Iterator;
import java.util.Map;
import java.util.Collections;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        HashMap<String, Object> genresMap = new HashMap<String, Object>();      //<장르, 곡 정보> 
        HashMap<String, Integer> playMap = new HashMap<String, Integer>(); //<장르, 총 장르 재생수>
        ArrayList<Integer> resultAL = new ArrayList<Integer>();

        for(int i = 0; i < genres.length; i++){
            String key = genres[i];
            HashMap<Integer, Integer> infoMap;       // 곡 정보 : <곡 고유번호, 재생횟수>

            if(genresMap.containsKey(key)){
                 infoMap = (HashMap<Integer, Integer>)genresMap.get(key);
            }
            else {
                infoMap = new HashMap<Integer, Integer>();
            }

            infoMap.put(i, plays[i]);
            genresMap.put(key, infoMap);

            //재생수
            if(playMap.containsKey(key)){
                playMap.put(key, playMap.get(key) + plays[i]);
            }
            else {
                playMap.put(key, plays[i]);
            }
        }

        int mCnt = 0;
        Iterator it = sortByValue(playMap).iterator();

        while(it.hasNext()){
            String key = (String)it.next();
            Iterator indexIt = sortByValue((HashMap<Integer, Integer>)genresMap.get(key)).iterator();
            int playsCnt = 0;

            while(indexIt.hasNext()){
                resultAL.add((int)indexIt.next());
                mCnt++;
                playsCnt++;
                if(playsCnt > 1) break;
            }
        }

        int[] answer = new int[resultAL.size()];

        for(int i = 0; i < resultAL.size(); i++){
            answer[i] = resultAL.get(i).intValue();
        }

        return answer;
    }

    private ArrayList sortByValue(final Map map){
        ArrayList<Object> keyList = new ArrayList();
        keyList.addAll(map.keySet());

        Collections.sort(keyList, new Comparator(){
            public int compare(Object o1, Object o2){
                Object v1 = map.get(o1);
                Object v2 = map.get(o2);

                return ((Comparable) v2).compareTo(v1);
            }
        });

        return keyList;
    }
}
```

- HashMap 형변환을 아래와 같이 사용할 수 있는 방법을 알게됐다.
```java
infoMap = (HashMap)genresMap.get(key);

if(genresMap.containsKey(key)){
        infoMap = (HashMap<Integer, Integer>)genresMap.get(key);
}
```

### Ref
1. https://unluckyjung.github.io/java/2020/12/19/Java_Overlay_Map/ (JAVA 중첩된 map 사용시 주의할 점)

​

2. https://stackoverflow.com/questions/2774608/how-do-i-access-nested-hashmaps-in-java (nested HashMaps in Java)

​

3. https://docs.oracle.com/javase/8/docs/api/java/util/Map.Entry.html (getKey 사용법)

​

4. https://www.delftstack.com/ko/howto/java/how-to-sort-a-map-by-value-in-java/ (hashmap 내림차 정렬)


#### 느낀점

nested hashmap을 처음 사용해 봐서 중구난방으로 짠것같다. 리팩토링을 해봐야겠다. 

그리고 이번 문제는 헷갈렸던 부분이 있었는데, 문제와 제한사항을 꼭 잘 읽어봐야겠다. 이것 때문에 시간이 너무 오래걸렸다.