import java.util.*;
public class ReverseAnArray {
    public static void reverse(int numbers[]){
        int start = 0;
        int end = numbers.length-1;
        while(start<end){
            //swapping using third variable
            //Remember temp is not an Index
            int temp = numbers[end];
            numbers[end]=numbers[start];
            numbers[start]=temp;

            start++;
            end--;

        }
    }
    public static void main(String args[]){
        int numbers[]={1,2,3,4,5};
        //call function to reverse array
        reverse(numbers);
        //print reveresed array
        for(int i=0;i<numbers.length;i++){
            System.out.print(numbers[i]+" ");
        }
        System.out.println();

    }
    
}
