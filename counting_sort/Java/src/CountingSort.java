import java.util.Arrays;

public class CountingSort {
    public Integer[] countingSort(Integer[] lista){
        int vMax = getMaxValue(lista);
        
        Integer[] countingValues;
        
        //Garantindo que o array de contagem gerado terá um tamanho minimamente igual ao de referência:
        if (vMax < lista.length) countingValues = new Integer[lista.length];
        else countingValues = new Integer[vMax+1];
        
        //Inicializando as posições do array:
        Arrays.fill(countingValues, 0);
        
        //Contagem de repetições de elementos:
        for (int n : lista) countingValues[n] += 1;
        
        Integer[] positions = new Integer[lista.length];
        Arrays.fill(positions, 0);
        
        int currentPosition = 0;
        int index = 0;
        for(int value : countingValues){
            for(int j = 0; j < value; j++){
                positions[currentPosition] = index;
                currentPosition++;
            }
            index++;
        }
        
        return positions;
    }
    
    private static int getMaxValue(Integer[] lista) {
        int max = Integer.MIN_VALUE;
        for (int n : lista) {
            if (n > max) {
                max = n;
            }
        }
        return max;
    }
    
    public static void main(String[] args){}
}
