import datetime
import sys

ORIGINAL_WRITE = sys.stdout.write


def my_write(string_text: str):
    if not string_text.rstrip():  # \n
        return
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    formatted_now = f"[{now}]: {string_text}\n"
    ORIGINAL_WRITE(formatted_now)


def main():
    sys.stdout.write = my_write
    print('1, 2, 3')
    sys.stdout.write = ORIGINAL_WRITE


if __name__ == '__main__':
    main()
