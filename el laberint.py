casos = int(input())


for _ in range(casos):
    
    H, W = map(int, input().split())

    laberint = []
    start = None
    finish = None
    
    for i in range(H):
        fila = input().strip()
        laberint.append(fila)
        
        if 'S' in fila:
            start = (i, fila.index('S'))
        if 'F' in fila:
            finish = (i, fila.index('F'))
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
   
    queue = [(start[0], start[1], 0)] 
    visited = set()
    visited.add(start)
    
    found = False
    while queue:
        
        x, y, steps = queue.pop(0)
        
        if (x, y) == finish:
            print(steps)
            found = True
            break
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < H and 0 <= ny < W and (nx, ny) not in visited:
                if laberint[nx][ny] == '.' or laberint[nx][ny] == 'F':
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))
    
    if not found:
        print("IMPOSSIBLE SORTIR")
