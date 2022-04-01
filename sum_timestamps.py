import math


# Bad solution - should have calculated the total time in seconds
def sum_timestamps(timestamps):
    minute = []
    second = []
    hour = []
    for time in timestamps:
        if len(time) < 6:
            add_minutes, add_seconds = time.split(":")
        else:
            add_hours, add_minutes, add_seconds = time.split(":")
            hour.append(int(add_hours))
        second.append(int(add_seconds))
        minute.append(int(add_minutes))
    output_seconds = sum(second)
    # Can use divmod for this instead
    if output_seconds >= 60:
        minute.append(math.floor(output_seconds / 60))
        output_seconds = output_seconds % 60
    output_minutes = sum(minute)
    if output_minutes >= 60:
        hour.append(math.floor(output_minutes / 60))
        output_minutes = output_minutes % 60
    output_hours = sum(hour)
    # Can use if hours:
    if output_hours < 1:
        # :02d} ensures that the seconds will have 2 digits
        return str(output_minutes) + ':' + f"{output_seconds:02d}"
    else:
        return str(output_hours) + ':' + f"{output_minutes:02d}" + ':' + f"{output_seconds:02d}"

"""
BETTER SOLUTION
def parse_time(time_string):
    minutes, seconds = time_string.split(':')
    return int(minutes) * 60 + int(seconds)


def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:01d}:{seconds:02d}"


def sum_timestamps(timestamps):
    total_time = sum(
        parse_time(time)
        for time in timestamps
    )
    return format_time(total_time)
"""


sum_timestamps(['5:32', '4:48'])
sum_timestamps(['03:10', '01:00'])
sum_timestamps(['2:10', '1:59'])
times = [
            '3:52', '3:29', '3:23', '4:05', '3:24', '2:29', '2:16', '2:44',
            '1:58', '3:21', '2:51', '2:53', '2:51', '3:32', '3:20', '2:40',
            '2:50', '3:24', '1:20', '3:22', '3:26', '0:42', '5:20']
sum_timestamps(times)
sum_timestamps(['02:01'])
sum_timestamps(['6:15:32', '2:45:48'])
sum_timestamps(['6:35:32', '2:45:48', '40:10'])