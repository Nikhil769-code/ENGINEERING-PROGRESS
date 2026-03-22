public class LinearSearchInStringArray{
    public static int search(String menu[], String key ){
        for(int i = 0 ; i<menu.length;i++){
            if(menu[i]== key){
                return i;
            }
        }return -1;
    }public static void main(String[] args) {
        String menu[] = {"idli","samosa","chai","dosa"};
        String key = "dosa";
        int index = search(menu, key);
        if(index == -1){
            System.out.println("Not Found ");
        }else{
            System.out.println("The index at which item found is :" + index);
        }
    }
}