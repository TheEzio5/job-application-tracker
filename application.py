class Application:
    def __init__(self,company,position, location, date, status):
        self.company = company
        self.position = position
        self.location = location
        self.date = date
        self.status = status
    def to_dict(self):
        return {
            "company": self.company,
            "position": self.position,
            "location": self.location,
            "date": self.date,
            "status": self.status
        }