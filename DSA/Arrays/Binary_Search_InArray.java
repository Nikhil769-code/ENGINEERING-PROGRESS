public class Binary_Search_InArray {
    //Here I declared the function of binary search
public static int binarysearch(int numbers[], int key){
   int start = 0;
   int end = numbers.length-1;//Last Element of the array

   while(start<=end){
    int mid = (start+end)/2;
    if(numbers[mid] == key){
        return mid;
    }
     else if(numbers[mid]<key){
        start= mid+1;
    }else{
        end = mid-1;
    }
}

   return -1;
}


    //Binary search only works on sorted arrays. (Very Important)
    public static void main(String args[]){
    int numbers[]={2,4,6,8,10,12,14};
    int key = 14;
    int index = binarysearch(numbers,key);
    if(index == -1){
        System.out.println("The Key not found !");
    }else{
        System.out.println(index);

    }   
 }
}

