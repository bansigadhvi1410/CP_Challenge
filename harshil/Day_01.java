// Q-link: https://www.codechef.com/problems/MEBA

import java.util.*;


/*If there is more than one unique element in the array (m.size() > 1) and there is more than one unique non-zero element (c > 1), it is impossible to make all elements equal using the given operation.
This is because:
Adding two different non-zero elements will result in a new value that is not necessarily equal to the other elements.
Thus, the array will always contain multiple unique values, and we cannot reduce it to a single repeating value.*/


class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t!=0){
            int n=sc.nextInt();
            int c=0;
            HashSet<Integer> h=new HashSet<>();
            for(int i=0;i<n;i++){
                int x=sc.nextInt();
                if(h.add(x)){
                    if(x!=0)
                        c++;
                }
            }
            if(c>1)
                System.out.println("no");
            
            else
                System.out.println("yes");
            
            t--;
        }
	}
}