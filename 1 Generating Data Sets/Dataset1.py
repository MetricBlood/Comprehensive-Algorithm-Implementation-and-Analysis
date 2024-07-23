import random

def generate_dataset1(seed):
    sizes = [100, 1000, 10000, 100000, 500000, 1000000]
    random.seed(seed)
    
    with open('dataset1.txt', 'w') as outfile:
        for index, size in enumerate(sizes):
            dataset = [random.randint(0, 100000) for _ in range(size)]
            outfile.write(f"Set {index + 1}:\n")
            outfile.write(" ".join(map(str, dataset)) + "\n\n")

if __name__ == "__main__":
    leader_id = 1211310073
    generate_dataset1(leader_id)
    print("Dataset 1 generated successfully.")
