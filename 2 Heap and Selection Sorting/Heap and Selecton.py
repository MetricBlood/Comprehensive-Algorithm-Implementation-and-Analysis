import time
import heapq
import os

def read_datasets(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    datasets = {}
    set_number = 1
    current_data = []
    for line in data:
        if line.startswith('Set'):
            if current_data:
                datasets[set_number] = current_data
                set_number += 1
            current_data = []
        else:
            current_data.extend(map(int, line.strip().split()))
    if current_data:
        datasets[set_number] = current_data
    return datasets

def heap_sort(data):
    heapq.heapify(data)
    sorted_data = [heapq.heappop(data) for _ in range(len(data))]
    return sorted_data

def selection_sort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

def write_dataset(filename, data):
    with open(filename, 'w') as file:
        file.write(' '.join(map(str, data)) + '\n')

def log_time(logfile, set_number, heap_time, selection_time):
    with open(logfile, 'a') as file:
        file.write(f'Set {set_number}: Heap Sort Time = {heap_time:.6f} seconds, Selection Sort Time = {selection_time:.6f} seconds\n')

def main():
    dataset_filename = 'dataset1.txt'  # Change this to the correct path if necessary
    if not os.path.exists(dataset_filename):
        print(f"Dataset file '{dataset_filename}' not found.")
        return
    
    print("Reading datasets...")
    datasets = read_datasets(dataset_filename)
    print("Datasets read successfully.")
    
    for set_number, data in datasets.items():
        print(f"Processing set {set_number}...")

        data_copy = data[:]
        
        start_time = time.time()
        heap_sorted_data = heap_sort(data)
        heap_sort_time = time.time() - start_time
        print(f"Heap sort completed for set {set_number} in {heap_sort_time:.6f} seconds.")
        
        start_time = time.time()
        selection_sorted_data = selection_sort(data_copy)
        selection_sort_time = time.time() - start_time
        print(f"Selection sort completed for set {set_number} in {selection_sort_time:.6f} seconds.")
        
        write_dataset(f'heap_sorted_set_{set_number}.txt', heap_sorted_data)
        write_dataset(f'selection_sorted_set_{set_number}.txt', selection_sorted_data)
        log_time('sorting_times.txt', set_number, heap_sort_time, selection_sort_time)
    
    print("Processing completed for all sets.")

if __name__ == '__main__':
    main()
