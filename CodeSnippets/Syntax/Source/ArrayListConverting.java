public class ArrayListConverting {

    public static void main(String[] args) {
        String[] array = {new String("David"), new String("John"), new String("Mike")};

        ArrayList<String> theArrayList = convertToArrayList(array);
    }

    private static ArrayList<String> convertToArrayList(String[] array) {
        ArrayList<String> convertedArray = new ArrayList<String>();

        for (String element : array) {
            convertedArray.add(element);
        }

        return convertedArray;
    }
}