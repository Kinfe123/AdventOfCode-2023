from heapq import heappush , heappop



grid = []

with open('./input.txt') as f:
    for inp in f:
        curr = inp.replace('\n' , '')
        grid.append([int(i) for i in curr])
seen = set()
heap = [(0, 0, 0, 0, 0, 0)]

while heap:
    loss, r, c, dr, dc, n = heappop(heap)
    
    if r == len(grid) - 1 and c == len(grid[0]) - 1 and n >= 4:
        print(loss)
        break

    if (r, c, dr, dc, n) in seen:
        continue

    seen.add((r, c, dr, dc, n))
    
    if n < 10 and (dr, dc) != (0, 0):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            heappush(heap, (loss + grid[nr][nc], nr, nc, dr, dc, n + 1))


    if n >= 4 or (dr , dc) == (0, 0):
        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr = r + ndr
                nc = c + ndc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    heappush(heap, (loss + grid[nr][nc], nr, nc, ndr, ndc, 1))
