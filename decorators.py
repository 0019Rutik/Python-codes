def dec1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("executed")
    return nowexec

@dec1
def why_is_harry():
    print("Harry is a good boy")

why_is_harry()
