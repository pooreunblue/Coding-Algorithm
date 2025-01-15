import java.util.Arrays;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int list[] = {a, b, c, d};
        int ans = 0;
        Arrays.sort(list);
        
        if(list[0] == list[3]) 
        {
            ans = 1111*list[0];
        } 
        else if (list[0] == list[2]) 
        {
            ans = (int)Math.pow((10*list[0]+list[3]),2);
        } 
        else if (list[1] == list[3]) 
        {
            ans = (int)Math.pow((10*list[1]+list[0]),2);
        } 
        else if (list[0] == list[1] && list[2] == list[3]) 
        {
            ans = (list[0] + list[2]) * Math.abs(list[0] - list[2]);
        } 
        else if(list[0] == list[1] || list[1] == list[2] || list[2] == list[3]) 
        {
            if (list[0] == list[1]) 
            {
                ans = list[2] * list[3];
            } 
            else if (list[1] == list[2]) 
            {
                ans = list[0] * list[3];
            } 
            else if (list[2] == list[3]) 
            {
                ans = list[0] * list[1];
            }
        } 
        else 
        {
            ans = list[0];
        }
        return ans;
    }
}