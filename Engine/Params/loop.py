update_methods = []
def sign_update(method): update_methods.append(method)
def unsign_update(method): update_methods.remove(method)

draw_methods = []
def sign_draw(method): draw_methods.append(method)
def unsign_draw(method): draw_methods.remove(method)

logic_methods = []
def sign_logic(method): logic_methods.append(method)
def unsign_logic(method): logic_methods.remove(method)


def Update(f):
    '''
    Registers update on this metod - 
    use only without args
    '''
    sign_update(f)
    return f

def Draw(f):
    '''
    Registers draw on this metod - 
    use only without args
    '''
    sign_draw(f)
    return f

def Logic(f):
    '''
    Registers logic on this metod - 
    use only without args
    '''
    sign_logic(f)
    return f