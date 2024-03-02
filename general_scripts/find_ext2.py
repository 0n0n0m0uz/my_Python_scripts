import os


def find_files_with_exclusion(start_dir, extension, exclusions):
    """
    Recursively find files with a given extension, excluding specified directories.

    :param start_dir: The directory to start the search from.
    :param extension: The file extension to search for (include the dot, e.g., '.txt').
    :param exclusions: A list of directories to exclude. These should be absolute paths
                       or paths relative to the start directory that will be excluded
                       from the search along with their subdirectories.
    """
    exclusions = [os.path.abspath(os.path.join(start_dir, exc)) for exc in exclusions]

    for root, dirs, files in os.walk(start_dir, topdown=True):
        # Modify dirs in place to skip over excluded directories
        dirs[:] = [
            d for d in dirs if os.path.abspath(os.path.join(root, d)) not in exclusions
        ]

        for file in files:
            if file.endswith(extension):
                print(os.path.join(root, file))


# Example usage
start_directory = "/mnt/c/Users/derek/"
file_extension = ".py"  # Example: looking for Python files
excluded_directories = [
    "anaconda3",
    "OneDrive/Desktop/Utilities",
    ".vscode",
    "AppData",
    "Tidal-Media-Downloader-2022.08.29.1",
    "Downloads/OD",
    "demucs"
]  # Relative to start_directory (no "/" to start with:  Downloads/Folder  ")

find_files_with_exclusion(start_directory, file_extension, excluded_directories)
