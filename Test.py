# print("Hello DSA, this file if for  testing purpose only.")
# class a:
#     def aa(self):
#         print("A")
#
#
# class b(a):
#     def bb(self):
#         print("B")
#
#
# class c(b):
#     def cc(self):
#         print("C")
#
#
# if __name__=="__main__":
#         cob=c()
#
#         cob.cc()
#         cob.bb()
#         cob.aa()

# Testing for recursion
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))
