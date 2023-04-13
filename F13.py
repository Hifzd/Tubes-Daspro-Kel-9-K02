from additional import splitter

def load(folder, csv):
    dat = open(f'{folder}/{csv}', 'r')
    matrix = splitter(dat.read(), '\n')
    return matrix