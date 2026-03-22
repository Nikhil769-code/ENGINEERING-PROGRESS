//Problem - Check for duplicates in the given array if yes then return the size of the array containing unique elements
// Pre-Requisite - The Array must be sorted
//TC- Optimal - o(n)
//SC - o(1)
// I have not done brute force method for this problem because it uses set which I have not studied yet.
public class checkduplicates {
    public static int duplicatecheck(int arr[]){
        int i=0;
        //j is starting from 1 because 0 index is always fixed for i=1 as this is a sorted array.
        for(int j=1;j<arr.length;j++){
            if(arr[j]!=arr[i]){
                //Store Unique element in front of current unique element
                arr[i+1]=arr[j];
                i++;
            }
        }return i+1;
    }
    public static void main(String args[]){
        int arr[]={1,2,2,3,3,4,4,5,5,6,6};
        System.out.println("The Size of Unique Array is : "+duplicatecheck(arr));
    }    
}
