from time import sleep, time


def ft_tqdm(lst):
    """
    ft_tqdm(lst) -> Iterable with progress bar

    Displays a progress bar while iterating over the given iterable.
    """
    try:
        total = len(lst)
    except TypeError:
        raise TypeError("Input must be an iterable")

    if total == 0:
        raise ValueError("Iterable is empty")

    start_time = time()
    progress = 0
    for elem in lst:
        progress += 1
        percentage = int(progress / total * 100)

        bar_length = 40
        filled_length = int(bar_length * progress // total)
        bar = '█' * filled_length + ' ' * (bar_length - filled_length)

        elapsed_time = time() - start_time

        if elapsed_time != 0:
            it_per_sec = progress / elapsed_time
        else:
            it_per_sec = 0

        if it_per_sec != 0:
            remaining_time = (total - progress) / it_per_sec
        else:
            remaining_time = 0

        elapsed_minutes = int(elapsed_time // 60)
        elapsed_seconds = int(elapsed_time % 60)
        elapsed_time_str = f"{elapsed_minutes:02d}:{elapsed_seconds:02d}"

        remaining_minutes = int(remaining_time // 60)
        remaining_seconds = int(remaining_time % 60)
        remaining_time_str = f"{remaining_minutes:02d}:{remaining_seconds:02d}"
        strpercentage = str(percentage) + '%'
        padding = 1 if percentage < 100 and percentage >0 else 0
        print(f'\r{strpercentage.rjust(3 + padding)}|{bar}| {progress}/{total} [{elapsed_time_str}<{remaining_time_str}, {it_per_sec:.2f}it/s]', end='', flush=True)

        yield elem


        
if __name__ == "__main__":
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
