import shutil
from time import time


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
    return f"{hours:02d}:{minutes:02d}"


def format_elapsed_time(start, end):
    elapsed = end - start
    hours = int(elapsed // 3600)
    minutes = int((elapsed % 3600) // 60)
    return f"{hours:02d}:{minutes:02d}"


def ft_tqdm(lst: range) -> None:
    """Function ft_tqdm mimics the behaviour of tqdm
and displays a progress bar"""
    start_time = time()

    try:
        length = len(lst)

        for i, item in enumerate(lst, start=1):
            terminal_width = shutil.get_terminal_size().columns
            time_now = time()

            percent = int(i / length * 100)
            text_front = f"{percent:3d}%"
            text_back = f" {i}/{length} \
[{format_elapsed_time(start_time, time_now)}\
<{estimated_remaining_time(length, i + 1, start_time)},  \
{average_speed(start_time, i + 1)}]"

            bar_length = max(10, terminal_width - len(text_front) -
                             len(text_back) - 5)

            filled = int(bar_length * (i / length))
            bar = "=" * filled + ">" + " " * (bar_length - filled)

            print(f"\r{text_front}|[{bar}]|{text_back}", end="", flush=True)

            yield item
    except TypeError as e:
        print(f"Type Error: {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
