from pathlib import Path


file_path = "C:/Users/User/Documents/example.txt"

def get_parent(_path_obj):
    return _path_obj.parent

def get_name(_path_obj):
    return _path_obj.stem

def get_suffix(_path_obj):
    return _path_obj.suffix

def parse_path(_path):
    p = Path(_path)
    parent = get_parent(p)
    name = get_name(p)
    suffix = get_suffix(p)
    return (parent, name, suffix)

print(parse_path(file_path))