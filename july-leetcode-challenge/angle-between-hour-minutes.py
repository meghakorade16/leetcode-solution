def angleClock(hour: int, minutes: int) -> float:
    angle = abs(6.0 * minutes - (hour * 30 + 0.5 * minutes))
    if angle >= 180:
        return 360 - angle
    else:
        return angle


if __name__ == '__main__':
    angleClock(3, 30)
