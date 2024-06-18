text = "The quick brown fox jumps over the lazy dog. Lazy dog, lazy fox!"

def check_ch(ch):
    if ch.isdigit():
        return ''
    elif ch == '"' or ch == "'":
        return ' '
    elif ch == '.' or ch == ',':
        return ''
    elif ch == '!' or ch == '?':
        return ''
    else:
        return ch.lower()

_1step = [(check_ch(ch)) for ch in text]
_2step = ''.join(_1step).split()

def get_f_values():
    final_dict_values = {}
    for item in _2step:
        _val = final_dict_values.get(item, '')
        if _val:
            final_dict_values[item] += 1
        else:
            final_dict_values[item] = 1
    return final_dict_values

def _print_me(_dict):
    print([(k, v) for k, v in sorted(_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)])

_print_me(get_f_values())