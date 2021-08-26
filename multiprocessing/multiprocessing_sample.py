import time
import concurrent.futures


def do_something(sec):
    time.sleep(sec)


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [i for i in range(5)]
        executor.map(do_something, secs)
