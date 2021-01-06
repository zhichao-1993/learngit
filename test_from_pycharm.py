import os
import datetime

def run_this():
    now = datetime.datetime.now()
    print("run_this in {} \n{}".format(os.getcwd(), now))

if __name__ == "__main__":
    run_this()