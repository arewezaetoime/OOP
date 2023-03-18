from calendar import month_name


class DVD:
    def __init__(self, name: str, dvd_id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.is_rented: bool = False
        self.name = name
        self.id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction

    @classmethod
    def from_date(cls, new_dvd_id: int, name: str, date: str, age_restriction: int):
        day, month, year = [int(d) for d in date.split('.')]

        return cls(name, new_dvd_id, year, month_name[month], age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction " \
               f"{self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"