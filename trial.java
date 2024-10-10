import java.util.Arrays;

public class ProjectProfit {

    public static int countValidPairs(int n, int[] profit, int[] implementationCost) {
        int[] netProfit = new int[n];
        
        // Calculate the net profit for each project
        for (int i = 0; i < n; i++) {
            netProfit[i] = profit[i] - implementationCost[i];
        }
        
        // Sort the net profits
        Arrays.sort(netProfit);
        
        int count = 0;
        int left = 0;
        int right = n - 1;
        
        // Use two-pointer technique to count valid pairs
        while (left < right) {
            if (netProfit[left] + netProfit[right] > 0) {
                // All pairs between left and right are valid
                count += (right - left);
                right--;
            } else {
                left++;
            }
        }
        
        return count;
    }

    public static void main(String[] args) {
        int n = 5;
        int[] profit = {2, 3, 7, 1, 1};
        int[] implementationCost = {3, 4, 5, 1, 2};
        
        int result = countValidPairs(n, profit, implementationCost);
        System.out.println("Number of valid pairs: " + result);  // Output should be 4
    }
}
