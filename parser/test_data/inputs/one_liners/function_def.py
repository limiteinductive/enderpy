def a(): pass

def a():
    pass

def a(a, b, c): pass

def a(a, *b, **c): pass

def a(a,
b,
c): pass

@decor
def a(): pass

@decor
def f(a: 'annotation', b=1, c=2, *d, e, f=3, **g): pass

def func() -> None: pass

async def a(): pass

async def a():
    pass

async def a(a, b, c): pass
