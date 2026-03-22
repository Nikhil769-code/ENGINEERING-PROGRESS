
public class Kadanes {
    //Kadane Algorithm For All Edge Cases Included
    public static void kadane(int arr[]){
        int currsum = arr[0];
        int maxsum = arr[0];
        for(int i = 1;i<arr.length;i++){
            currsum = Math.max(arr[i],currsum+arr[i]);
            maxsum = Math.max(currsum,maxsum);
            
            // currsum+=arr[i];
            // //If current sum is negative then make it zero.
            // if(currsum<0){
            //     currsum=0;
            // }
            // //Checks maximum element between current sum and maximum sum.
            // maxsum=Math.max(currsum,maxsum);
        }
        System.out.println("The Max Sum of Sub-Array is : "+maxsum);

    }
    public  static void main(String args[]){
        //int arr[]={-2,-3,4,-1,-2,1,5,-3};
        int arr[]={-2,-3,-4,-1,-2,-1,-5,-3};
            kadane(arr);
        };
    }

//Edge Case - If The array consits of all negative elements , then --> the max sum should not be 0 , so the above method is correct.