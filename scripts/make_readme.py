
def write_doc(module, filename):
    with open(filename, 'w') as f:
        f.write(module.__doc__)
