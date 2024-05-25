import java.util.*;

public class PracticaConSebas {
    public static int findCenter(int[][] edges) {
        int[] res = edges[0];
        int[] edge = edges[1];
        int ans = 0;
        if (res[0] == edge[0] || res[0] == edge[1]) {
            ans = res[0];
            System.out.printf("res = %s\n", res[0]);
        }
        else {
            ans = res[1];
            System.out.printf("res = %s\n", res[1]);
        }
        return ans;
//        Arrays.sort(res);
//        for (int i = 1; i < edges.length ; i++) {
//            int[] edge = edges[i];
//            Arrays.sort(edge);
//            if (Arrays.equals(res, edge)){
//                continue;
//            }
//            else {
//                if (edge[0] == res[0]) {
//                    ans = edge[0];
//                }
//                else {
//                    ans = edge[1];
//
//                }
//            }
//        }
    }

    public static boolean findPath (int n, int[][] edges) {
        HashMap<Integer, List<Integer>> graph = new HashMap<>();
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; i++) graph.put(i, new ArrayList<>());
        for (int[] edge : edges) {
            System.out.println(Arrays.toString(edge));
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        System.out.println(graph);
        return dfs(graph, 0, 5, visited);
    }

    public static boolean dfs (HashMap<Integer, List<Integer>> graph, int start, int end, boolean[] visited) {
        System.out.println("start = " + start);
        System.out.println("edge = " + graph.get(start));
        if (start == end) return true;
        visited[start] = true;
        for (int neighbor : graph.get(start)) {
            if (!visited[neighbor]) {
                if (dfs(graph, neighbor, end, visited)) return true;
            }
        }
        return false;
    }

    public static

    public static void main(String[] args) {
        //[[0,1],[0,2],[3,5],[5,4],[4,3]]
        int n = 6;
        int[][] edges = {{0,1},{0,2},{3,5},{5,4},{4,3}};
//        findCenter(edges);
//        System.out.println(findPath(n, edges));
    }
}