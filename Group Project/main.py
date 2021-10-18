import subprocess as sp
from utils.cursor import con
from utils.insert import insert_user,insert_product

OPTIONS = """
Choose the option corresponding to the action you want to perform:
0. Exit [EXIT]
1. Add a new user [INSERT]
2. Add a new product [INSERT]
Option: """


def dispatch(opt):
    functions = {
        0: exit,
        1: insert_user,
        2: insert_product,
    }
    functions[opt]()

def main():
    _ = sp.call('clear', shell=True)
    if not con.open:
        print("There was an error connecting to database")
        exit(0)    
    while(True):
        _ = sp.call('clear', shell=True)
        opt = int(input(OPTIONS))
        dispatch(opt)
        _ = input("Press enter to continue...")

if __name__ == "__main__":
    main()

        


