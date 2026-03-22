public class SubArrays {
    public static void printsubarrays(int arr[]){
        int totalsubarr = 0;
        for(int i=0;i<arr.length;i++){
           
            for(int j=i;j<arr.length;j++){
                totalsubarr++;
                for(int k=i;k<=j;k++){
                    System.out.print(arr[k]+" ");
                    
                }System.out.println();
            }
        }System.out.println(totalsubarr);
    }
    public static void main(String args[]){
        int arr[]= {1,2,3,4,5,6,7,8};
        printsubarrays(arr);

    }
    
}
