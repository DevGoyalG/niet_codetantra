# Q13 (again answer updated)

n = int(input())
m = int(input())

graph = [[] for _ in range(n)]
for _ in range(m):
	u, v = map(int, input().split())
	graph[u].append(v)
	        
start_vertex = int(input())
	        
def bfs(graph, start_vertex):
	visited = [False] * len(graph)
	queue = [start_vertex]
	        	            
	while stack:
		vertex = stack.pop(0)
		if not visited[vertex]:
			print(vertex, end=' ')
			visited[vertex] = True
			for neighbor in graph[vertex]:
				if not visited[neighbor]:
					stack.append(neighbor)
bfs(graph, start_vertex)
