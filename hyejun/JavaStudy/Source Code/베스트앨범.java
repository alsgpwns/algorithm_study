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