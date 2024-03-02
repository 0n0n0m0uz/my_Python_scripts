def read_csv(filename):
    with open(filename) as fp:
        from csv import reader
        data_rows = list(reader(fp))
    header = data_rows.pop(0)
    return (header, data_rows)


# Read the math class data
math_header, math_data_rows = read_csv('student-mat.csv')

# Read the Portuguese class data
port_header, port_data_rows = read_csv('student-por.csv')

# Print a sample of the data


def print_sample(header, data, num_rows=5):
    from math import floor, log10
    fmt = "Row {{:0{}d}}: {{}}".format(floor(log10(num_rows)) + 1)
    string_rows = [fmt.format(i, str(r))
                   for i, r in enumerate(data[:num_rows])]
    print("--> Header ({} columns): {}".format(len(header), header))
    print("\n--> First {} of {} rows:\n{}".format(num_rows,
                                                  len(data),
                                                  '\n'.join(string_rows)))

# print("=== Math data ===\n")
# print_sample(math_header, math_data_rows)
