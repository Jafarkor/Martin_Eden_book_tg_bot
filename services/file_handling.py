import os
import sys

BOOK_PATH = 'book/Book.txt'
PAGE_SIZE = 700

book: dict[int, str] = {}

def _my_rfind(text, start, fin):
    syms = '.!?;'
    stop = start
    for sym in syms:
        now = text.rfind(sym, start, fin)
        if now > stop:
            stop = now
    return stop


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    stop = _my_rfind(text, start, start + size)
    while (stop+1 < len(text)) and (text[stop+1] in '.!?;'):
        stop = _my_rfind(text, start, stop)
    return text[start:stop+1], len(text[start:stop+1])


def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    start, page_number = 0, 1
    while start < len(text):
        page_text, length = _get_part_text(text, start, PAGE_SIZE)
        book[page_number] = page_text.lstrip()
        start += length
        page_number += 1




prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))