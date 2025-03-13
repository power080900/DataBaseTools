import os
import pandas as pd

def get_folder_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def human_readable_size(size, decimal_places=2):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if size < 1024:
            return f"{size:.{decimal_places}f} {unit}"
        size /= 1024

def check_and_print_stats(root_path):
    result = []
    for dirpath, dirnames, filenames in os.walk(root_path):
        dataset = dirpath.split('\\')[1]
        if 'rawdata' in dirnames:
            if 'labeldata' in dirnames:
                rawdata_path = os.path.join(dirpath, 'rawdata')
                labeldata_path = os.path.join(dirpath, 'labeldata')        

        elif 'Images' in dirnames:
            if 'Labels' in dirnames:
                rawdata_path = os.path.join(dirpath, 'Images')
                labeldata_path = os.path.join(dirpath, 'Labels')
        else:
            continue
        rawdata_size, rawdata_count = get_folder_size(rawdata_path)
        labeldata_size, labeldata_count = get_folder_size(labeldata_path)
        label_readable_size = human_readable_size(labeldata_size)
        raw_readable_size = human_readable_size(rawdata_size)
        print(f'{dataset}: rawdata size: {raw_readable_size}, rawdata count: {rawdata_count}, labeldata size: {label_readable_size}, labeldata count: {labeldata_count}')
        result.append((dataset, labeldata_count, rawdata_count,  label_readable_size, raw_readable_size))
    return result

def main():
    base_path = 'Z:\\'
    datasets = [i for i in os.listdir(base_path)]

    for dataset in datasets:
        rawdata_path = os.path.join(base_path, dataset,'data', 'IR', 'rawdata')
                    
        if os.path.exists(rawdata_path):
            print(rawdata_path)
            size = get_folder_size(rawdata_path)
            print(f'{rawdata_path}: {size / (1024 * 1024):.2f} MB')

        else:
            print(f'{rawdata_path} does not exist')
    
    for dataset in datasets:
        rawdata_path = os.path.join(base_path, dataset,'data', 'DEPTH', 'rawdata')
                    
        if os.path.exists(rawdata_path):
            print(rawdata_path)
            size = get_folder_size(rawdata_path)
            print(f'{rawdata_path}: {size / (1024 * 1024):.2f} MB')

        else:
            print(f'{rawdata_path} does not exist')

if __name__ == "__main__":
    main()