from calculator import square
def main():
        test_square()
def test_square():
    try:
        assert square(2)==4
    except AssertionError:
        print("test failed for 2")
    try:
        assert square(3)==9
    except AssertionError:
        print("test failed for 3")    
    try:
        assert square(0)==0
    except AssertionError:
        print("test failed for 0")
    try:
        assert square(-2)==4
    except AssertionError:
        print("test failed for -2")    
    

if __name__=="__main__":
        main()