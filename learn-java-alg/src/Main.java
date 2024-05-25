import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main {
    public static List<Integer> prefix_sum_list(List<Integer> ar, int start, int end) {
        List<Integer> prefix_sum = new ArrayList<>();
        prefix_sum.add(0);
        for (int i = 0; i < ar.size(); i++) {
            prefix_sum.add(prefix_sum.get(i) + ar.get(i));
        }
        return prefix_sum;
    }

    public static Integer[] prefix_sum_array(int[] ar, int start, int end) {
        Integer[] prefix_sum = new Integer[ar.length+1];
        prefix_sum[0] = 0;
        for (int i = 0; i < ar.length; i++) {
            prefix_sum[i+1] = prefix_sum[i] + ar[i];
        }
        return prefix_sum;
    }

    public static void main(String[] args) {
        int[] ar = {-1,-1,0,1,1,0};
        Integer[] prefix_ar = prefix_sum_array(ar, 0, ar.length);
        System.out.printf("prefix_ar = %s\n", Arrays.toString(prefix_ar));
        for (int i = 1; i < prefix_ar.length; i++) {
            int left = prefix_ar[i-1];
            int right = prefix_ar[ar.length] - prefix_ar[i];
            System.out.printf("left = %s, right = %s\n", left, right);
            if (left == right){
                System.out.printf("%s", i-1);
                return;
            }
        }
        System.out.printf("-1");
    }

    public static void solution(String[] args) {
        List<Integer> ar = new ArrayList<>(
                List.of(-4,-3,-2,-1,4,3,2)
        );
        String s = "00";
        List<Integer> ar_zeros = new ArrayList<>();
        List<Integer> ar_ones = new ArrayList<>();
        ar_zeros.add(0);
        ar_ones.add(0);
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '0'){
                ar_zeros.add(ar_zeros.get(i) + 1);
                ar_ones.add(ar_ones.get(i));
            }
            else if (s.charAt(i) == '1') {
                ar_zeros.add(ar_zeros.get(i));
                ar_ones.add(ar_ones.get(i) + 1);
            }
        }
        int max = 0;
//        ar_ones.get()
        System.out.printf("ar_zeros = %s\n", ar_zeros);
        System.out.printf("ar_ones = %s\n", ar_ones);
        for (int i = 1; i < s.length(); i++) {
            int currentMax = ar_zeros.get(i) + (ar_ones.get(ar_ones.size()-1) - ar_ones.get(i));
            if (currentMax>max)
                max = currentMax;
        }
        System.out.printf("max = %s\n", max);

    }
}