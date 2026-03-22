public class Prefix_Sum {
    public static void prefixsum(int arr[]){
        //Declare The Prefix array of same size as the declared array
        int prefix[]=new int[arr.length];
        int maxsum = Integer.MIN_VALUE;

        //calculate prefix array
        prefix[0]=arr[0];
        for(int i=1; i<prefix.length;i++){
            prefix[i]=prefix[i-1]+arr[i];
        }
         
        for(int i=0;i<arr.length;i++){
            for(int j=i;j<arr.length;j++){
                int currsum=0;
                //Ternary Operator 
                //If starting index == 0 then index will become negative which is incorrect . So , currsum becomes prefix[j] --> Which is sum till last index 
                currsum = i == 0 ? prefix[j]:prefix[j]-prefix[i-1];
                    if(maxsum<currsum){
                        maxsum=currsum;
                    }

            }
        }System.out.println("Max sum from sub arrays is : "+maxsum);
    }
    public static void main(String args[]){
        int arr[]= {1,-2,6,-1,3};
        prefixsum(arr);
    }
    
}
