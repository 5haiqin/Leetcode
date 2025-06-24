class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.bookings:
            if start < endTime and startTime < end:
                return False
        self.bookings.append((startTime, endTime))
        return True
