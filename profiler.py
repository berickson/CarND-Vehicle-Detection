import collections
import time

class Profiler:    
    def __init__(self):
        self.durations = collections.defaultdict(float)
        self.counts = collections.defaultdict(int)
        self.current_operation = None
        self.start_time = None
    def reset(self):
        self.__init__()
    def end(self):
        if self.current_operation is not None:
            o = self.current_operation
            duration = time.time() - self.start_time
            self.counts[o] += 1
            self.durations[o] += duration
            self.start_time = None
            self.current_operation = None

    def start(self,operation):
        self.end()
        self.current_operation = operation
        self.start_time = time.time()
        
    def report(self):
        operations = list(self.counts.keys())
        operations.sort()
        for o in operations:
            print ('"{}" duration: {:.2f} count: {}'.format(o,self.durations[o],self.counts[o]))