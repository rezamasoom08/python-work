import time
def causeError():
    start = time.time()
    try:
        time.sleep(0.5)
        return 1/0
    except Exception as e:
        print(e)
    finally:
        print(f'Function took {time.time() - start} seconds to execute')

causeError()

