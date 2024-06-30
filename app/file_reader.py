

def read_content(f: str):
    try:
        with open(f, 'r') as file:
            content = file.read()
    except IsADirectoryError:
        content = " Work In Progress !"
    return content
