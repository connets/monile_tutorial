def merge_intervals(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0]) # sort intervals by start time
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:  # sovrapposizione
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged