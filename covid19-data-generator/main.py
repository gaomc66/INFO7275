from Generators import generator
import time


def main():
    start_at = time.perf_counter()
    generator.generator()
    end_at = time.perf_counter()
    print(f"{end_at - start_at:0.4f}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
