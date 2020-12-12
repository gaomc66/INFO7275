from Generators import generator
import time


# main function
def main():
    start_at = time.perf_counter()
    generator.generator()
    end_at = time.perf_counter()
    print(f"{end_at - start_at:0.4f}")


if __name__ == '__main__':
    main()

