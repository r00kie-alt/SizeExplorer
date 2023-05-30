import os

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def get_total_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        total_size += get_folder_size(dirpath)
    return total_size

def get_subfolder_sizes(parent_folder):
    subfolder_sizes = {}
    for entry in os.scandir(parent_folder):
        if entry.is_dir():
            subfolder_path = entry.path
            subfolder_name = entry.name
            subfolder_size = get_total_folder_size(subfolder_path)
            subfolder_sizes[subfolder_name] = subfolder_size
    return subfolder_sizes

def format_size(size, unit):
    units = {
        1: 'bytes',
        2: 'kilobytes',
        3: 'megabytes',
        4: 'gigabytes',
        5: 'terabytes'
    }
    if unit in units:
        return size / (1024 ** (unit - 1))
    else:
        return size

# Get user input for parent directory path, size unit, and sort order
parent_folder_path = input("Enter the parent directory path: ")
size_unit_choice = int(input("Choose the size unit:\n1. Bytes\n2. Kilobytes\n3. Megabytes\n4. Gigabytes\n5. Terabytes\n"))
sort_order = input("Enter the sort order (asc for ascending, desc for descending): ")

subfolder_sizes = get_subfolder_sizes(parent_folder_path)

# Sort the subfolder sizes based on the sort order
if sort_order.lower() == 'asc':
    subfolder_sizes = sorted(subfolder_sizes.items(), key=lambda x: x[1])
else:
    subfolder_sizes = sorted(subfolder_sizes.items(), key=lambda x: x[1], reverse=True)

# Print the sizes of each subfolder with the desired unit
units = {
    1: 'bytes',
    2: 'kilobytes',
    3: 'megabytes',
    4: 'gigabytes',
    5: 'terabytes'
}
for subfolder, size in subfolder_sizes:
    formatted_size = format_size(size, size_unit_choice)
    unit = units[size_unit_choice]
    print(f"{subfolder}: {formatted_size:.2f} {unit}")
