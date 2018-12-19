import os, sys


if __name__ == '__main__':
    account_name = os.environ['JAVA_HOME']
    sys.stdout.write(account_name)
    sys.stdout.flush()
    # sys.stderr.write("it is sys.stderr.write")
    # sys.stderr.flush()