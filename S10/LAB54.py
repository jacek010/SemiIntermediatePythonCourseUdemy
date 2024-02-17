import os
import itertools


def scantree(start_path):
    for entry in os.scandir(start_path):
        if entry.is_dir():
            yield entry
            yield from scantree(entry.path)
        else:
            yield entry


listing = scantree('LAB52_files')
for lst in listing:
    print('DIR' if lst.is_dir() else 'FILE', lst.path)

listing = scantree('LAB52_files')
listing = sorted(listing, key=lambda e: e.is_dir())

for is_dir, elements in itertools.groupby(listing, lambda e: e.is_dir()):
    print('DIR' if is_dir else 'FILE', len(list(elements)))

