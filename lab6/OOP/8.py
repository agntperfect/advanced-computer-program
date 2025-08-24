class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __eq__(self, other):
        return (self.hours == other.hours and
                self.minutes == other.minutes and
                self.seconds == other.seconds)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"


t1 = Time(10, 30, 15)
t2 = Time(10, 30, 15)
t3 = Time(12, 45, 0)

print(f"t1 = {t1}")
print(f"t2 = {t2}")
print(f"t3 = {t3}")

print("t1 == t2 ?", t1 == t2)
print("t1 == t3 ?", t1 == t3)