class TVController():
    
    def __init__(self, channels, channel = 0):
        self.channels = channels
        self.channel = channel
    
    def first_channel(self):
        self.channel = 0
        return self.channels[0]
    
    def last_channel(self):
        self.channel = len(self.channels) - 1
        return self.channels[-1]
    
    def turn_channel(self, n):
        self.channel = n - 1
        return self.channels[n-1]
    
    def next_channel(self):
        self.channel += 1
        return self.channels[self.channel]
    
    def previous_channel(self):
        self.channel -= 1
        return self.channels[self.channel]
    
    def current_channel(self):
        return self.channels[self.channel]
    
    def is_exist(self, name = None):
        if name in self.channels:
            return "Yes"
        return "No" 
    
channels = ["BBC", "Discovery", "TV1000"]

controller = TVController(channels)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist("BBC"))