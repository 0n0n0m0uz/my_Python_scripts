def dump_head(filename, max_lines=5):
    from sys import stdout
    from math import log10, floor
    lines = []
    with open(filename) as fp:
        for _ in range(max_lines):
            lines.append(fp.readline())
    stdout.write("\n=== First {} lines of: '{}' ===\n\n".format(
        max_lines, filename))
    for line_num, text in enumerate(lines):
        fmt = "[{{:0{}d}}] {{}}".format(floor(log10(max_lines)) + 1)
        stdout.write(fmt.format(line_num, text))
    stdout.write('.\n.\n.\n')


# dump_head('student-mat.csv')
# dump_head('student-por.csv')
