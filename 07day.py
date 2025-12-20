# What is differnece between (*args,**kwargs)

def test(*args,**kwargs):
    print(args)
    print(kwargs)
test(1,2,a=3)