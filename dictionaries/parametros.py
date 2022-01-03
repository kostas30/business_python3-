def new(name, *data):
    print(name, ",epitheto:", data[0], ",tel:", data[1])


new("kostas", "messinis", 2548953)


def new(name, **data):
    print(name, data)


new("kostas", epitheto="messinis", tel= 2548953)


def new(name, **data):
    print("name:", name)
    for key, value in data.items():
        print(f'{key}: {value}')


new("kostas", epitheto="messinis", tel= 2548953)
