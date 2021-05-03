package totallyNewSnippets;

public class IsMaxHeap {

    public static void main(String[] args) {
        int[] data = {6, 2, 3, 1, 2, 0, 4};
        System.out.println(isMaxHeap(data, 0));
    }

    public static boolean isMaxHeap(int[] data, int current){
        int left = current * 2 + 1;
        int right = current * 2 + 2;

        if(left < data.length){
            if(data[current] < data[left]){
                return false;
            }else if(!isMaxHeap(data, left)){
                return false;
            }
        }

        if(right < data.length){
            if(data[current] < data[right]){
                return false;
            }else if(!isMaxHeap(data, right)){
                return false;
            }
        }

        return true;
    }
}