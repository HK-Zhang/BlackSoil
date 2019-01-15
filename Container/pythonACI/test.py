import os, sys
import time

if __name__ == '__main__':
    account_name = os.environ['JAVA_HOME']
    # sys.stdout.write(account_name)
    # sys.stdout.flush()
    time_start=time.time()
    time.sleep(10)
    time_end=time.time()
    print time_end-time_start
    # sys.stderr.write("it is sys.stderr.write")
    # sys.stderr.flush()