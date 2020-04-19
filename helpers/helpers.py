def ticket_printer(name, seat, movie, time):
    text = f"| Customer: {name} Seat: {seat} Movie: {movie} Time: {time} |"
    frame = f"+{'-' * (len(text) - 2)}+"
    empty_frame = f"|{' ' * (len(text) - 2)}|"

    border = [frame, empty_frame, text, empty_frame, frame]
    border_text = "\n".join(border)
    print(border_text)