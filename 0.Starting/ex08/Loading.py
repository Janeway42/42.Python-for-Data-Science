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
        print(f"len: {length}")

        for i, item in enumerate(lst, start=1):
            percent = i / length
            filled = int(bar_length * percent)
            bar = '=' * filled + '>' + ' ' * (bar_length - filled)
            time_now = time()

            percent_completed = int(percent * 100)
            # visual alignment of percentage completed
            beautifying_space_percent = " " * (3 - len(str(percent_completed)))
            # visual alignment of the step number completed
            beautifying_space_steps = " " * (len(str(length)) - len(str(i)))

            print(f"{beautifying_space_percent}{percent_completed}%|[{bar}]| \
                  {beautifying_space_steps}{i}/{length} \
                    [{format_elapsed_time(start_time, time_now)} < \
                    {estimated_remaining_time(length, i + 1, start_time)}, \
                    {average_speed(start_time, i + 1)}]")

            yield item
    except TypeError as e:
        print(f"Type Error: {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
