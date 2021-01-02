class Cinema:
    def __init__(self, time, room):
        self.time = time
        self.room = room

        rows, letters = self.room.seating_plan()
        self.seats = [None] + [{letter: None for letter in letters} for __ in rows]

    def get_day(self):
        return self.time[:3]

    def get_hour(self):
        return self.time[3:]

    def get_movie(self):
        return self.room.get_name()

    def _parse_seats(self, seat="10B"):
        rows, letters = self.room.seating_plan()

        letter = seat[-1]

        if letter not in letters:
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat number {row_text}")

        if row not in rows:
            raise ValueError(f"Row {row} is out of range")

        return row, letter

    def allocate_person(self, person="Jan K.", seat="10B"):
        row, letter = self._parse_seats(seat)

        if self.seats[row][letter] is not None:
            raise ValueError(f"Seat {seat} is already occupied")

        self.seats[row][letter] = person

    def relocate_person(self, seat_from, seat_to):
        row_from, letter_from = self._parse_seats(seat_from)

        if self.seats[row_from][letter_from] is None:
            raise ValueError(f"No person on {seat_from} seat.")

        row_to, letter_to = self._parse_seats(seat_to)

        if self.seats[row_to][letter_to] is not None:
            raise ValueError(f"Seat {seat_to} is already taken.")

        self.seats[row_to][letter_to] = self.seats[row_from][letter_from]
        self.seats[row_from][letter_from] = None

    def get_empty_seats(self):
        return sum(sum(1 for seat in row.values() if seat is None)
                   for row in self.seats
                   if row is not None)

    def print_tickets(self, printer):
        persons = self.get_list_of_people()

        for person, seat in persons:
            printer(person, seat, self.get_movie(), self.time)

    def get_list_of_people(self):
        persons = []
        rows, letters = self.room.seating_plan()

        for row in rows:
            for letter in letters:
                person = self.seats[row][letter]
                if person is not None:
                    person_data = person, f"{row}{letter}"
                    persons.append(person_data)

        return persons
