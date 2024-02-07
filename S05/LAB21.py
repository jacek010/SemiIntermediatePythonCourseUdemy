import os
import functools
from datetime import datetime as dt


def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            with open(log_file_path, "a") as f:
                f.write(f"Action type: {logged_action} | Path: {path} | Time: {dt.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.close()
            result = func(path)
            return result
        return the_real_wrapper
    return wrapper_with_log_to_known_file


@wrapper_with_log_file(logged_action="FILE_CREATE", log_file_path='LAB21_files/file_create_logs.txt')
def create_file(path):
    print('creating file {}'.format(path))
    open(path,"w+")


@wrapper_with_log_file(logged_action="FILE_DELETE", log_file_path='LAB21_files/file_delete_logs.txt')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r'LAB21_files/dummy_file.txt')
delete_file(r'LAB21_files/dummy_file.txt')
create_file(r'LAB21_files/dummy_file.txt')
delete_file(r'LAB21_files/dummy_file.txt')