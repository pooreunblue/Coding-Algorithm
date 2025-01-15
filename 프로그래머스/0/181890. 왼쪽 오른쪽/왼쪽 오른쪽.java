import java.util.Arrays;

class Solution {
    public String[] solution(String[] strList) {
	String[] answer = {};
	int indexOfL = Arrays.asList(strList).indexOf("l");
	int indexOfR = Arrays.asList(strList).indexOf("r");
	if(indexOfL != -1 && (indexOfR == -1 || indexOfL < indexOfR)) {
		return Arrays.copyOf(strList, indexOfL);
	} else if(indexOfR != -1 && (indexOfL == -1 || indexOfL > indexOfR)) {
		return Arrays.copyOfRange(strList, indexOfR+1, strList.length);
	}
        return answer;
    }
}