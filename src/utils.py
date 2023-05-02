
def getExecTime(start, end):
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)
    if hours > 0:
        return f"{int(hours)}h {int(minutes)}min {seconds:.2f}s"
    elif minutes > 0:
        return f"{int(minutes)}min {seconds:.2f}s"
    else:
        return f"{seconds:.2f}s"
