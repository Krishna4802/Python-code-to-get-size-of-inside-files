import zipfile
import os
import datetime
from tabulate import tabulate

def get_file_info(zip_file_path):
    file_info = []
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        for info in zip_ref.infolist():
            file_name = os.path.basename(info.filename)  # Extract only the file name without the directory path
            file_size = info.file_size
            # Convert file size to MB and round off to 2 digits
            file_size_mb = round(file_size / (1024 * 1024), 2)
            timestamp = datetime.datetime(*info.date_time)
            file_info.append((file_name, file_size_mb, timestamp))
    return file_info

def process_directory(directory):
    table_data = []
    for file_name in os.listdir(directory):
        if file_name.endswith(".zip"):
            zip_file_path = os.path.join(directory, file_name)
            zip_file_info = get_file_info(zip_file_path)
            for info in zip_file_info:
                table_data.append([file_name, info[0], info[1], info[2]])
    headers = ["Zip filename", "Inside File name", "Size (MB)", "Created timestamp"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Example usage:
directory_path = 'path/to/your/directory'  # Directory containing zip files
process_directory(directory_path)
