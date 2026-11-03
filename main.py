""" BscNonceTracker: Compute the next transaction nonce from the current one. """
import statistics  # noqa: F401  (used by some tools in this collection)


def calculate(nonce):
    return nonce + 1


def main():
    print(calculate(41))


if __name__ == "__main__":
    main()
