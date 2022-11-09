from os import remove
from os import walk
from os.path import join
from hashlib import md5
from filecmp import cmp
from base64 import b64encode

def md5_checksum(file_path):
    """ Returns the raw MD5 bytes here used as checksum a given files content """

    with open(file_path, "rb") as f:
        file = f.read()
    m = md5()
    m.update(file)
    return m.digest(), file_path


def md5_checksum_table(dir_name, suffix):
    """
    Searches a directory for files with a given file format (a suffix) and
      computes their MD5 checksums.
    """
    table = {}
    for root, _, files in walk(dir_name):
        for file in files:
            if file.endswith(suffix):
                checksum, filename = md5_checksum(join(root, file))
                table.setdefault(checksum, []).append(filename)
    return table


def print_duplicates(checksums):
    """ Prints paths of files have the same MD5 checksum and are identical. """

    for checksum, paths in checksums.items():
        if len(paths) > 1:
            print('Files have the checksum {0} are:\n {1}'.format(b64encode(checksum),
                                                                  "\n".join(paths)))
            if any(cmp(x, y) for x in paths for y in paths if y != x):
                # print('\nThey are identical\n')
                kill(paths)


def kill(paths):
    """ Delete all files in the list except for first item"""
    
    for extra in paths[1:]:
        print(extra + ' be deleted!')
        remove(extra)


if __name__ == '__main__':
    FOLDER = r"D:\Rilla\"
    table = md5_checksum_table(FOLDER, '.txt')
    print_duplicates(table)
