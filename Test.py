# print("Hello DSA")
class a:
    def aa(self):
        print("A")


class b(a):
    def bb(self):
        print("B")


class c(b):
    def cc(self):
        print("C")


if __name__=="__main__":
        cob=c()

        cob.cc()
        cob.bb()
        cob.aa()