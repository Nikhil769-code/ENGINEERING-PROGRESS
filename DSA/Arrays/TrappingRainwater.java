public class TrappingRainwater {
    //Function to calculate Total Trapped Water
    public static int trappedwater(int height[]){
        // We Require 3 things --> leftmax,rightmax and totaltrappedwater
        int twater = 0;
        int n = height.length;
        //define new arrays leftmax[] and rightmax[] of same length as auxillary array
        int leftmax[] = new int[height.length];
        int rightmax[] = new int[height.length];
        rightmax[n-1]=height[n-1];
        leftmax[0]=height[0];
        //Left max = Bar with maximum height at the left of current bar
        for(int i = 1; i<n;i++){
            leftmax[i]= Math.max(height[i],leftmax[i-1]);
        }
        //Right max = Bar with maximum height at the right of current bar
        for(int i = n-2;i>=0;i--){
            rightmax[i]= Math.max(height[i],rightmax[i+1]);
        }
        //Maximum water level / water level for a bar  = Minimum of (leftmax,rightmax)
        //Trapped water = current water level - height of current bar 
        for(int i = 0 ; i<n;i++){
             int waterlevel = Math.min(leftmax[i],rightmax[i]);
             //This calculates the total trapped water ;
             twater += waterlevel - height[i];

        }
        
        return twater;
    }
    public static void main(String args[]){
        //This is the auxillary array which includes the heights of bars.
    int height[] = {4,2,0,6,3,2,5};
    //The total trapped water is stored in result 
    int result = trappedwater(height);
    //Print The result
    System.out.println("Total Trapped Water : "+result);
    }
}
