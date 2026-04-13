#include <stdio.h>
#include <limits.h>
#include <stdbool.h>

#define MAX 1005

int graph[MAX][MAX];
int dist[MAX];
bool visited[MAX];

int main() {
    int n, m;

    printf("Enter number of cities (vertices) and roads (edges): ");
    scanf("%d %d", &n, &m);

    // initialize graph
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            graph[i][j] = 0;
        }
    }

    printf("Enter edges in format (u v w):\n");
    printf("u = city A, v = city B, w = distance/time between them\n");

    for (int i = 0; i < m; i++) {
        int u, v, w;

        // u = starting city
        // v = destination city
        // w = distance or time between city u and v
        scanf("%d %d %d", &u, &v, &w);

        graph[u][v] = w;
        graph[v][u] = w; // since roads are two-way
    }

    int start, end;
    printf("Enter start city and destination city: ");
    scanf("%d %d", &start, &end);

    // initialize distances
    for (int i = 1; i <= n; i++) {
        dist[i] = INT_MAX;
        visited[i] = false;
    }

    dist[start] = 0;

    // Dijkstra Algorithm
    for (int i = 1; i <= n; i++) {
        int u = -1, min = INT_MAX;

        for (int j = 1; j <= n; j++) {
            if (!visited[j] && dist[j] < min) {
                min = dist[j];
                u = j;
            }
        }

        if (u == -1) break;

        visited[u] = true;

        for (int v = 1; v <= n; v++) {
            if (graph[u][v] && !visited[v]) {
                if (dist[u] + graph[u][v] < dist[v]) {
                    dist[v] = dist[u] + graph[u][v];
                }
            }
        }
    }

    // output
    if (dist[end] == INT_MAX)
        printf("No Path Exists\n");
    else
        printf("Shortest distance from %d to %d is: %d\n", start, end, dist[end]);

    return 0;
}