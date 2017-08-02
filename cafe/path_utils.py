import os

# ATTENTION : This file need to be at the root path because of get_app_base_path pmethod


def get_app_base_path():
    return os.path.dirname(os.path.realpath(__file__))


def get_folder_path_from_root_project(path):
    return os.path.join(get_app_base_path(), path)
