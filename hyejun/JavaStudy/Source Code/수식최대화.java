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