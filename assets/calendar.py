class Calendar:
    def __init__(self):
        self.events = []

    def add_event(self, event, date=None):
        self.events.append((event, date))
    
    def view_events(self):
        for event, date in self.events:
            print(f"{date}: {event}")

    def count_events_by_month(self, month):
        count = sum(1 for _, date in self.events if date.startswith(month))
        return count
