
public class Array_as_function_arguments{
    //This is the method that changes the elements of array when it is passed as object.
    public static int change(int marks[],int fixed){
        for(int i = 0; i<marks.length;i++){
            //Updation condition
        marks[i] = marks[i]*2;
        }
    fixed = 10;
    return fixed;
    }
    public static void main(String args[]){
        int marks[] = {1,2,3};
        int fixed = 5;
        //Here the method is called 
        fixed =  change(marks, fixed);
        for(int i = 0 ; i <marks.length;i++){
            System.out.println(marks[i]);
        }
        // Here we check that the value of fixed has changed or not .
        System.out.println(fixed);
    }
        
}
