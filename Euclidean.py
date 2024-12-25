
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
points = [(1, 2), (3, 4), (6, 8), (2, 1)]

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)


min_distance = min(distances)
print("Minimum Öklid mesafesi:", min_distance)
