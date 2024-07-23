def read_dataset(filename):
    stars = []
    with open(filename, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            star_data = line.strip().split('|')
            if len(star_data) == 6:
                name = star_data[0].strip()
                x, y, z, weight, profit = map(int, star_data[1:])
                stars.append([name, x, y, z, weight, profit])
    return stars

def knapsack(S, W):
    n = len(S)
    B = [0] * (W + 1)
    selected_items = [[0] * (W + 1) for _ in range(n)]

    for k in range(1, n + 1):
        for w in range(W, S[k - 1][1] - 1, -1):
            if B[w - S[k - 1][1]] + S[k - 1][0] > B[w]:
                B[w] = B[w - S[k - 1][1]] + S[k - 1][0]
                selected_items[k - 1][w] = 1
    
    # Determine selected items
    selected = []
    weight = W
    for i in range(n - 1, -1, -1):
        if selected_items[i][weight] == 1:
            selected.append((S[i][1], S[i][0]))
            weight -= S[i][1]
            
    return B[W], selected


filename = "dataset2.txt"
stars = read_dataset(filename)
stars2 = read_dataset(filename)
stars = [(star[5], star[4]) for star in stars]
capacity = 800
max_profit, selected_items = knapsack(stars, capacity)
           
output_filename = "Stars_Conquered.txt"
with open(output_filename, 'w') as output_file:
    output_file.write("Maximum profit: {}\n".format(max_profit))
    output_file.write("Stars travelled:\n")
    for weight, profit in selected_items:
        for star in stars2:
            if star[4] == weight and star[5] == profit:
                output_file.write("{}\n".format(star))

print("Output saved to", output_filename)
