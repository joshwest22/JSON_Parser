parsed = {}
filename = "easy_test.json"

def parse_s(s):
    print("parse_s called") #works
    if (s[0] == '{'):
        #add the literal value to dictionary
        pass
    else:
        reason = "some specific reason"
        print("Error! {reason}")

def main():
    print("Hello World!")
    with open(filename, "r") as file:
        data = file.read()
    parse_s(data)


if __name__ == "__main__":
    main()
