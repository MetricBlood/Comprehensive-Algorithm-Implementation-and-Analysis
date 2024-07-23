import random
import math
import string

STAR_COUNT = 20
ROUTE_COUNT = 54

def calculate_distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def generate_dataset2(seed):
    random.seed(seed)
    
    stars = list(string.ascii_uppercase[:STAR_COUNT])
    
    star_data = {star: {
        'x': random.randint(0, 1000),
        'y': random.randint(0, 1000),
        'z': random.randint(0, 1000),
        'weight': random.randint(1, 100),
        'profit': random.randint(1, 100)
    } for star in stars}
    
    routes = set()
    for star in stars:
        connections = set()
        while len(connections) < 3:
            potential_star = random.choice(stars)
            if star != potential_star:
                connections.add(potential_star)
        for conn in connections:
            routes.add(tuple(sorted((star, conn))))

    while len(routes) < ROUTE_COUNT:
        star1, star2 = random.sample(stars, 2)
        routes.add(tuple(sorted((star1, star2))))
    
    connections = {star: [] for star in stars}
    for star1, star2 in routes:
        distance = calculate_distance(
            star_data[star1]['x'], star_data[star1]['y'], star_data[star1]['z'], 
            star_data[star2]['x'], star_data[star2]['y'], star_data[star2]['z']
        )
        connections[star1].append((star2, distance))
        connections[star2].append((star1, distance))
    
    with open('dataset22.txt', 'w') as outfile:
        # Write header for star data
        outfile.write("Name\t|\tx\t|\ty\t|\tz\t|\tweight\t|\tprofit\n")
        outfile.write("----------------------------------------------------\n")
        
        # Write star data
        for star in stars:
            data = star_data[star]
            outfile.write(f"{star}\t|\t{data['x']}\t|\t{data['y']}\t|\t{data['z']}\t|\t{data['weight']}\t|\t{data['profit']}\n")
        
        # Write separator after star data
        outfile.write("----------------------------------------------------\n")
        outfile.write("Connections and Distances:\n")
        
        # Write connections and distances
        for star, conns in connections.items():
            outfile.write(f"{star}: ")
            conn_strings = [f"{conn_star} ({dist:.2f})" for conn_star, dist in conns]
            outfile.write(", ".join(conn_strings) + "\n")

if __name__ == "__main__":
    member_ids = [1191102837, 1221303182, 1211100574]
    sum_ids = sum(member_ids)
    generate_dataset2(sum_ids)
    print("Dataset 2 generated successfully.")
