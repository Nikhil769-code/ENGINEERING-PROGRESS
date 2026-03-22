public class LargestNum {
    public static int getLargest(int numbers[]){
        int largest = Integer.MIN_VALUE;
        int smallest = Integer.MAX_VALUE;
        for(int i = 0 ; i<numbers.length;i++){
            if(largest<numbers[i]){
                largest=numbers[i];
            }
         }
        for(int i = 0;i<numbers.length;i++){
            if(smallest>numbers[i]){
                smallest = numbers[i];
            }
        } System.out.println("The Smallest Value is : "+ smallest);
         
         return largest;
         
    }public static void main(String[] args) {
        int numbers[]={1,3,5,8,9};
        System.out.println("The Largest Value is : "+ getLargest(numbers));
    }
 }
