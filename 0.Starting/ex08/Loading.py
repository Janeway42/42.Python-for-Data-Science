import argparse
from time import time
from time import sleep

def average_speed(start_time, items_done):
    elapsed_time = time() - start_time
    speed_rate = items_done / elapsed_time if elapsed_time > 0 else 0 
    return f"{speed_rate:.2f}it/s"

def estimated_remaining_time(items, items_done, start_time):
    elapsed_time = time() - start_time
    items_left = items - items_done
    average_time_per_item = elapsed_time / items_done

    estimated_time_left = items_left * average_time_per_item

    hours = int(estimated_time_left // 3600)
    minutes = int((estimated_time_left % 3600) // 60)
    seconds = int(estimated_time_left % 60)
    miliseconds = int((estimated_time_left - int(estimated_time_left)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}:{miliseconds:02d}"

def format_elapsed_time(start, end):
    elapsed = end - start
    hours = int(elapsed // 3600)
    minutes = int((elapsed % 3600) // 60)
    seconds = int(elapsed % 60)
    miliseconds = int((elapsed - int(elapsed)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}:{miliseconds:02d}"

def ft_tqdm(lst: range) -> None:
    bar_length = 50
    start_time = time()

    try:
        length = len(lst)

        for i, item in enumerate(lst):
            percent = (i + 1) / length
            filled = int(bar_length * percent)
            bar = '=' * filled + '>' + ' ' * (bar_length - filled)
            time_now = time()

            percent_completed = int(percent * 100)
            beautifying_space_percent = " " * (3 - len(str(percent_completed)))
            beautifying_space_items = " " * (len(str(length)) - len(str(i + 1)))

            print(f"{beautifying_space_percent}{percent_completed}%|[{bar}]| {beautifying_space_items}{i + 1}/{length} [{format_elapsed_time(start_time, time_now)}<{estimated_remaining_time(length, i + 1, start_time)}, {average_speed(start_time, i + 1)}]")

            yield item
    except TypeError as e:
        print(f"Type Error: {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

def main(input_range):
    for item in ft_tqdm(range(input_range)):
        sleep(0.01)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="Script that filters strings based on the length of the words"
        )
    parser.add_argument("items", nargs="*", help="text to be analysed and word size")
    args = parser.parse_args()

    if len(args.items) != 1:
        print("bad, bad arguments")
    else:
        try:
            assert args.items[0].isdigit(), "not a number"
            main(int(args.items[0]))
        except (ValueError, AssertionError) as e:
            print("AssertionError:", e)
        