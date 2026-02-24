from datetime import date, datetime

# 13.1 Write current date to file
today = date.today()

with open("today.txt", "w") as file:
    file.write(str(today))

# 13.2 Read file into string
with open("today.txt", "r") as file:
    today_string = file.read()

# 13.3 Parse the date from the string
parsed_date = datetime.strptime(today_string, "%Y-%m-%d").date()


# 15.1
def worker(proc_num: int):
    wait_seconds = random.random()
    time.sleep(wait_seconds)

    # Print current time (include process number so output is clear)
    current_time = datetime.now().strftime("%H:%M:%S.%f")
    print(
        f"Process {proc_num} waited {wait_seconds:.3f}s, time: {current_time}")


def run_multiprocessing_demo():
    processes = []
    for i in range(1, 4):
        p = mp.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    # Wait for all processes to finish before the program exits
    for p in processes:
        p.join()


if __name__ == "__main__":
    date_file_tasks()
    run_multiprocessing_demo()
