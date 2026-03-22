public class Print_pairs {
    //Function To Print Pairs
    public static void printpairs(int arr[]){
        //Also Added calculation for Total Pairs
        int totalpairs = 0;

        for(int i=0;i<arr.length;i++){
            //Prints all pairs for current element
            int curr = arr[i];
            for(int j = i+1;j<arr.length;j++){
                System.out.print("("+ curr+","+arr[j]+")");
                totalpairs++;
            }System.out.println();
        }System.out.println("Total Pairs : "+ totalpairs);
    }
    public static void main(String args[]){
        int arr[] = {2,4,6,8,10};
        printpairs(arr);
    }
    
}
