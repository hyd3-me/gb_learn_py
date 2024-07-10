import unicodedata


FILE_PATH = '.output_task1.data.swp'
WRITE_PATH = '/media/haru/space_me/gb.data'

def get_ch(b_ch):
	try:
		ch = chr(b_ch)
		e_ch = ch.encode('utf-8', 'ignore')
		d_ch = e_ch.decode('utf-8', 'ignore')
		if unicodedata.category(d_ch)[0] == "C":
			return ''
		if not d_ch.isascii():
			return ''
		else:
			return d_ch
	except Exception as e:
		return ''

def get_decode_line(b_line):
	try:
		return b_line.decode('utf-8', error='ignore')
	except Exception as e:
		return ''

def get_utf_char(b_str):
	final_line = ''
	for char in b_str:
		decoded_char = get_ch(char)
		if decoded_char:
			final_line += decoded_char
	return final_line

def ma_reader(f_path):
	with open(f_path, 'rb') as file:
		while line124 := file.read(1024):
			yield get_utf_char(line124)
	return ''

def write_data(f_path, _data):
	with open(f_path, 'a+') as _file:
		_file.write(_data)

def main():
	for data in ma_reader(FILE_PATH):
		write_data(WRITE_PATH, data)
	return 0, 'ok'


if __name__ == '__main__':
	main()
