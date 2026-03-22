//Problem - Check if the array is sorted
//TC- o(n)
//SC - o(n)
//Pattern - arr[i]<=arr[j]
public class checksort{
    public static int sortedcheck(int arr[]){
        int i=0;
        for (int j=1;j<arr.length;j++){
            if(arr[i]<=arr[j]){
                i++;
            }else{
                return -1;
            }
        }return 1;
    }
    public static void main(String args[]){
        int arr[]= {1,2,2,3};
        int result = sortedcheck(arr);
        if(result==1){
            System.out.println("The Array is Sorted ");
        }else{
            System.out.println("The Array is Unsorted ");
        }

    }
}