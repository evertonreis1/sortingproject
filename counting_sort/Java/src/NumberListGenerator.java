import java.util.Random;

public class NumberListGenerator {
    Random r = new Random();
    
    public Integer[] getIntegerList(int range, int length){
        Integer[] list = new Integer[length];
    
        for(int i = 0; i < list.length; i++){
            int n = r.nextInt(range);
            list[i] = n;
        }
        
        return list;
    }
    
    public static void main(String[] args){}
}
