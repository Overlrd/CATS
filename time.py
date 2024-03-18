    hour = int(s[:2])
    if 'PM':
        if hour < 12:
            hour = hour + 12
        elif hour == 12:
            pass
    else:
        if hour == 12:
            hour = 0

    return str(hour)+s[2:-2]
