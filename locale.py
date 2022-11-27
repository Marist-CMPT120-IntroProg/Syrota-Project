class Locale:
    
    def __init__(self, name, summary, details):
        self.name = name
        self.summary = summary
        self.details = details
        self.was_visited = False
        
    def __str__(self):
        return "{}".format(self.summary) if self.was_visited == False else "You are at {}".format(self.name)
    
    #Mutator method
    def set_status_visited(self, status):
        self.was_visited = status
        
    #Observer method 
    def examine_command(self):
        return self.details

