public class Main {
    public static void main(String[] args){
        CountingSort cs = new CountingSort();
        NumberListGenerator nlg = new NumberListGenerator();
        
        //Todas as listas tem 1M de elementos
        Integer[] lista1 = nlg.getIntegerList(10, 1000000);  //intervalo de valores atribuídos e tamanho do array
        Integer[] lista2 = nlg.getIntegerList(100, 1000000);
        Integer[] lista3 = nlg.getIntegerList(1000, 1000000);
        Integer[] lista4 = nlg.getIntegerList(10000, 1000000);
        Integer[] lista5 = nlg.getIntegerList(100000, 1000000);
        Integer[] lista6 = nlg.getIntegerList(1000000, 1000000);
        Integer[] lista7 = nlg.getIntegerList(10000000, 1000000);  //max
        
        long start, end, m1 = 0, m2 = 0, m3 = 0, m4 = 0, m5 = 0, m6 = 0, m7 = 0;
        
        for(int i = 0; i < 1000; i++){
            //Teste na lista 1
            start = System.currentTimeMillis();
            cs.countingSort(lista1);
            end = System.currentTimeMillis();
            
            m1 = (m1 + (end - start))/2;
    
            //Teste na lista 2
            start = System.currentTimeMillis();
            cs.countingSort(lista2);
            end = System.currentTimeMillis();
    
            m2 = (m2 + (end - start))/2;
    
            //Teste na lista 3
            start = System.currentTimeMillis();
            cs.countingSort(lista3);
            end = System.currentTimeMillis();
    
            m3 = (m3 + (end - start))/2;
    
            //Teste na lista 4
            start = System.currentTimeMillis();
            cs.countingSort(lista4);
            end = System.currentTimeMillis();
    
            m4 = (m4 + (end - start))/2;
    
            //Teste na lista 5
            start = System.currentTimeMillis();
            cs.countingSort(lista5);
            end = System.currentTimeMillis();
    
            m5 = (m5 + (end - start))/2;
    
            //Teste na lista 6
            start = System.currentTimeMillis();
            cs.countingSort(lista6);
            end = System.currentTimeMillis();
    
            m6 = (m6 + (end - start))/2;
    
            //Teste na lista 7
            start = System.currentTimeMillis();
            cs.countingSort(lista7);
            end = System.currentTimeMillis();
    
            m7 = (m7 + (end - start))/2;
        }
        
        System.out.println("Tempo de execução médio (0 a 9): " + m1 + " ms.");
        System.out.println("Tempo de execução médio (0 a 99): " + m2 + " ms.");
        System.out.println("Tempo de execução médio (0 a 999): " + m3 + " ms.");
        System.out.println("Tempo de execução médio (0 a 9999): " + m4 + " ms.");
        System.out.println("Tempo de execução médio (0 a 99999): " + m5 + " ms.");
        System.out.println("Tempo de execução médio (0 a 999999): " + m6 + " ms.");
        System.out.println("Tempo de execução médio (0 a 9999999): " + m7 + " ms.");
    }
}
