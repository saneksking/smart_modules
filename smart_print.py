import shutil


def smart_print(text='', symbol='-'):
    if not text:
        msg = f'{text}'
    else:
        msg = f' {text} '
    width, _ = shutil.get_terminal_size()
    print(f'{msg}'.center(width, symbol))
