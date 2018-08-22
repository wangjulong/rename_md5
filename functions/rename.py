import os
from hashlib import md5


def main(dir_root="D:\work\images"):
    dirs = os.listdir(dir_root)

    for temp in dirs:
        original_dir = os.path.join(dir_root, temp)
        if os.path.isfile(original_dir):
            fmd5 = get_file_md5(original_dir)
            file_name, extension = temp.split('.')
            path_new = '{0}\{1}.{2}'.format(dir_root, fmd5, extension)
            print("old: ", original_dir)
            print("new: ", path_new)
            os.rename(original_dir, path_new)
        else:
            print(">>> This is a directory: ", original_dir)


def get_file_md5(filename):
    hmd5 = md5()
    fp = open(filename, "rb")
    hmd5.update(fp.read())
    return hmd5.hexdigest()


if __name__ == '__main__':
    main()
