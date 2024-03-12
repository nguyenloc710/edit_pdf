import os


def get_all_files_in_folder(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths


# Specify the folder path
folder_path = 'C:/CFM/DE/account-statistic-service-anh-hieu/CarDoctor AutoISM'

# Get all file paths in the folder and its subfolders
file_paths = get_all_files_in_folder(folder_path)

# Print the list of file paths
print(len(file_paths))
