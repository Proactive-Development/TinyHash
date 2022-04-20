import sys
from modules.algorithms import small , large

def file():
    use_small = False
    use_large = False
    for i in sys.argv:
        if i == "-s":
            use_small = True
        if i == "-l":
            use_large = True
    if use_small and use_large:
        print("Please choose only one algorithm")
        sys.exit()
    elif use_small == False and use_large == False:
        print("Please choose an algorithm")
        sys.exit()
    elif use_small == True and use_large == False:
        try:
            print(small.generate(open(sys.argv[-1], "r").read()))
        except FileNotFoundError:
            print("File not found")
            sys.exit()
        except:
            print("Something went wrong with trying to open"+ sys.argv[1])
            sys.exit()
    elif use_small == False and use_large == True:
        try:
            print(large.generate(open(sys.argv[-1], "r").read()))
        except FileNotFoundError:
            print("File not found")
            sys.exit()
        except:
            print("Something went wrong with trying to open"+ sys.argv[1])
            sys.exit()

if __name__ == "__main__":
    version = "1.0.0"
    use_small = False
    use_large = False
    for i in sys.argv:
        if i == "-v":
            print("Version:"+ version)
            sys.exit()
        if i == "--file":
            file()
        if i == "-s":
            use_small = True
        if i == "-l":
            use_large = True

    if use_small and use_large:
        print("Please choose only one algorithm")
        sys.exit()
    elif use_small == False and use_large == False:
        print("Please choose an algorithm")
        sys.exit()
    elif use_small == True and use_large == False:
        print(small.generate(sys.argv[-1]))
    elif use_small == False and use_large == True:
        print(large.generate(sys.argv[-1]))
