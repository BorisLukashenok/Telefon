def print_str(data):
    for i, v in enumerate(data, 1):
        print(f"{i}) {v}")


def print_list(data):
    print("-" * 22)
    for i in data:
        if i != '':
            for j in i.split(', '):
                print(f'|| {j}' + " " * (22 - len(j) - 5) + "||")
            print("-" * 22)
            print("-" * 22)
