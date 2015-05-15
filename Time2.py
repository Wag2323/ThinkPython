

class Time(object):
    """Represents the time of day"""

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
        
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
            
    def __radd__(self, other):
        return self.__add__(other)
        
    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
        
    def print_time(self):
        print '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def time_to_int(self):
        """Computes the number of seconds since midnight"""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
    
def print_attributes(obj):
    print 'The attributes of %s, %s are:' % (obj, obj.__class__)
    for attr in obj.__dict__:
        print attr, getattr(obj, attr)


if __name__ == '__main__':

    start = Time()
    start.hour = 9
    start.minute = 45
    start.second = 00

    start.print_time()
    seconds = start.time_to_int()
    print seconds
    end = start.increment(1337)
    end.print_time()
    print end.is_after(start)
    
    time = Time(9, 45, 7)
    print time
    time2 = Time(1, 1, 1)
    print time2
    sum = time + time2
    print sum
    sum2 = time + 140
    print sum2
    print 140 + time
    print_attributes(time)