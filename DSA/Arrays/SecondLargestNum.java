public class SecondLargestNum {
    public static void secondsmallest(int arr[]){
        int smallest = arr[0];
        int ssmallest = Integer.MAX_VALUE;
        for(int i = 0; i<arr.length;i++){
            if(arr[i]<smallest){
                ssmallest=smallest;
                smallest=arr[i];
            }else if(arr[i]!=smallest && arr[i]<ssmallest){
                ssmallest = arr[i];

            }
            
        }System.out.println("The smallest element in the array is : "+smallest);
        System.out.println("The second smallest element in the array is : "+ssmallest);
    }
    public static void getsecondlargest(int numbers[]){
        int largest = numbers[0];
        int slargest = Integer.MIN_VALUE;
        for(int i = 0;i<numbers.length;i++){
            if(numbers[i]>largest){
                slargest=largest;
                largest = numbers[i];
            }else if(numbers[i]<largest && numbers[i]>slargest){
                slargest=numbers[i];
            }
        }System.out.println("The largest element is : "+largest);
        System.out.println("The second largest element is : "+slargest);
    }
    public static void main(String args[]){
    int numbers[]= {-1,-2,-6,-8,-10};
    getsecondlargest(numbers);
    secondsmallest(numbers);

    }
}
