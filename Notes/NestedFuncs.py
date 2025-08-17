def outer(a, b):
    c = "c"
    
    def inner():
        return a + b + c
    
    return inner()

def main():
    result = outer("a", "b")
    print(result)

if __name__ == "__main__":
    main()
