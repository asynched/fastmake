import itertools


def flat(source: list) -> list:
    return list(itertools.chain(*source))
