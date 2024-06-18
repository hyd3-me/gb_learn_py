import pathlib


def rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc"):
    cur_dir = pathlib.Path().cwd()
    _name_target_dir = 'test_folder'
    target_dir = cur_dir / _name_target_dir
    count = 1
    for f_path in target_dir.iterdir():
        if not f_path.is_file():
            continue
        if f_path.stem == 'test':
            continue
        file_number = str(count).zfill(num_digits)
        new_file_path = f_path.with_name(f'{desired_name}{file_number}')
        if target_ext:
            new_file_path = new_file_path.with_suffix(f'.{target_ext}')
        else:
            new_file_path = new_file_path.with_suffix(f'.{source_ext}')
        if new_file_path.exists():
            continue
        f_path.rename(new_file_path)
        count += 1


if __name__ == '__main__':
    rename_files()