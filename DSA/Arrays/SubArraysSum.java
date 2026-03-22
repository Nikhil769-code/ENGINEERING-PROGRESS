public class SubArraysSum {
    public static void sumsubarrays(int arr[]){
        int largestsum = Integer.MIN_VALUE;
        int smallestsum = Integer.MAX_VALUE;
        for(int i=0;i<arr.length;i++){
            for(int j=i;j<arr.length;j++){
                int sum=0;
                System.out.print("Sub-Array"+"["+i+","+j+"]"+": ");
               /*Sum is Initialized here becuase if we don't,
                the sum value won't reset to 0 for next sub-array 
                and it will start adding sum of previous sub-array 
                This is brute force method with worst time complexity
                */
                for(int k=i;k<=j;k++){
                    sum+=arr[k];
                    System.out.print(arr[k]+" ");
                }
                if(sum>largestsum){
                    largestsum=sum;
                }
                if(sum<smallestsum){
                    smallestsum = sum;
                }
                System.out.println("  -> Sum : "+sum);
            }
        }System.out.println("The Largest Sum from all sub-arrays is :"+largestsum);
        System.out.println("The Smallest Sum from all sub-arrays is :"+smallestsum);
    }
    public static void main(String args[]){
        int arr[]= {1,2,3,4};
        sumsubarrays(arr);


    }
}
