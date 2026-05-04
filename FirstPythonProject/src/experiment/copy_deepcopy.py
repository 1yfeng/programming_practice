class Solution:
    def f(self):
        pass






if __name__ == "__main__":
    a = [2,3,4,5,8,7,[1,2]]
    b = a[2:]
    
    print(f"a={a}")
    print(f"b={b}")
    b[1] = 1000
    b[-1][1] = 1000
    print(f"a={a}")
    print(f"b={b}")