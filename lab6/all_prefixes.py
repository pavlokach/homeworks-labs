def get_all(line):
    out = []

    for i in range(len(line)):
        out.append(line[:i + 1])
    return out


def all_prefixes(line):
    first = line[0]
    out = get_all(line)
    line = line[1:]
    while first in line:
        line = line[line.index(first):]
        for elem in get_all(line):
            out.append(elem) if elem not in out else None
        line = line[1:]
    return set(out)
