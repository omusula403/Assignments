import sys
import numpy as np
def main():
    A=np.arange(1,5).reshape(2,2)
    B=np.arange(6,10).reshape(2,2)
    print (f"A={A}")
    print(f"B={B}")
    print(f"A+B={A+B}")
    print (f"A*B={A*B}")
    print(f"A@B={A@B}")

    return 0
if __name__ == "__main__":
    sys.exit(main())