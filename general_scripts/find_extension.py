import os
import fnmatch


def find_files(directory, extension, excluded_dirs):
    """
    Recursively searches for files with a given extension in a directory,
    excluding specified directories.

    :param directory: The root directory to search.
    :param extension: The file extension to search for.
    :param excluded_dirs: A list of directories to exclude from the search.
    """
    for root, dirs, files in os.walk(directory, topdown=True):
        # Exclude specified directories
        dirs[:] = [d for d in dirs if os.path.join(root, d) not in excluded_dirs]

        for file in files:
            if fnmatch.fnmatch(file, f"*.{extension}"):
                print(os.path.join(root, file))


# Example usage
directory_to_search = "/mnt/c/Users/derek/"
file_extension = "py"  # Without dot
directories_to_exclude = ["/mnt/c/Users/derek/anaconda3/", "/mnt/c/Users/derek/OneDrive/Desktop/Utilities/", "/mnt/cUsers/derek/.vscode/"]

find_files(directory_to_search, file_extension, directories_to_exclude)
