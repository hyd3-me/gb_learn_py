
def get_dir_size(_path):
    return 0

def save_results_to_json(_res, _fpath):
    with open(_fpath, 'w') as _file:
        json.dump(_res, _file)
    return 0

def save_results_to_csv(_res, _fpath):
    fieldnames = ['Path', 'Type', 'Size']
    with open(_fpath, 'w', newline='
') as _file:
        writer = csv.DictWriter(_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(_res)
    return 0

def save_results_to_pickle(_res, _fpath):
    with open(_fpath, 'wb') as _file:
        pickle.dump(_res, _file)
    return 0
def traverse_directory(_path):
    dir_crawler(_path)
    return get_result_list()
