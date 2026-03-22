public class stocksbuyandsell {
    //Function for Caluclating maximum profit
    public static void profit(int prices[]){
        int buyprice =Integer.MAX_VALUE;
        int maxprofit = 0;
        //Single Pass Loop
        for(int i = 0; i<prices.length;i++){
            //Condition-1    If buyprice is less then we calculate profit which is = selling price - min buyprice at that time 
            if(buyprice<prices[i]){
                int profit = prices[i]-buyprice;//today's profit
                //We calculate the maximum profit after comparing all profits simulatneously
                maxprofit = Math.max(profit,maxprofit);
            }else{
                //This works for first iteration where  the value of buyprice changes for infinity to prices[i] and also  IT SETS BUY PRICE TO MINIMUM 
                buyprice=prices[i];
            }
        }System.out.println("The Maximum Profit is : "+maxprofit);
    }
    public static void main(String args[]){
        int prices[]= {7,1,5,3,6,4};
        profit(prices);
    }
    
}
