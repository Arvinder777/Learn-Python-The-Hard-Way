
def scan(command):
    '''
    :param command: command user input
    :return: tuple which contains set of matching definition
    '''
    # first split command
    words = command.split()

    ret = []
    for word in words:
        try:
            ret += [('number', int(word))]
        except ValueError:
            low = word.lower()
            if low == 'north':
                ret += [('direction', 'north')]
            elif low == 'south':
                ret += [('direction', 'south')]
            elif low == 'east':
                ret += [('direction', 'east')]
            elif low == 'go':
                ret += [('verb', 'go')]
            elif low == 'kill':
                ret += [('verb', 'kill')]
            elif low == 'eat':
                ret += [('verb', 'eat')]
            elif low == 'bear':
                ret += [('noun', 'bear')]
            elif low == 'princess':
                ret += [('noun', 'princess')]
            else:
                ret += [('error', word)]

    return ret