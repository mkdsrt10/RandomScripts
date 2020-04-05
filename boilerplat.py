class Main(object):
    """docstring for Main."""
    def __init__(self):
        super(Main, self).__init__()
        # self.arg = arg
    def main(self):
        print self
        print type(self)
        print repr(self)
        print type(repr(self))

if __name__ == "__main__":
    print 'ff'
    Main().main()
