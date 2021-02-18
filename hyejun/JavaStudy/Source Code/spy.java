import java.util.*;

class Solution_Spy {
    public int solution(String[][] clothes) {
        int answer=1;
        HashMap<String,Integer> map = new HashMap<String, Integer>();

		for(int i=0; i<clothes.length; i++) {
			if(map.containsKey(clothes[i][1])) {
				int temp=map.get(clothes[i][1]);
				map.put(clothes[i][1], ++temp);
			}
			else map.put(clothes[i][1], 1);
		}

     
       if(map.size()==1) return clothes.length;
        
       for (String key : map.keySet()) {
			answer = answer * (map.get(key) + 1);
		}

        return answer-1;
    }
}