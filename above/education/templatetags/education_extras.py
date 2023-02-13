import itertools

from django import template

register = template.Library()


@register.filter
def chunks(value, chunk_len: int):
    """
        Example:
            value: [1, 2, 3, 4, 5, 6, 7, 8]
            chunk_len: 3

            Result: [1, 2, 3], [4, 5, 6], [7, 8]
    """
    seq_iter = iter(value)
    while True:
        chunk = list(itertools.islice(seq_iter, chunk_len))
        if chunk:
            yield chunk
        else:
            break
