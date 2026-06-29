class Application:
    def __init__(self,company,position, country, date, status):
        self.company = company
        self.position = position
        self.country = country
        self.date = date
        self.status = status
    def to_dict(self):
        return {
            "company": self.company,
            "position": self.position,
            "country": self.country,
            "date": self.date,
            "status": self.status
        }