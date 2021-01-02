from pprint import pprint
from cinema import Cinema
# from movie import Movie
from films import *
from helpers import *


def buy_a_ticket():

    greenmile = The_Green_Mile()
    # print(greenmile.num_seats())
    shawredemption = The_Shawshank_Redemption()
    # print(shawredemption.num_seats())
    # print(greenmile.get_name())
    f = Cinema("MON15", greenmile)
    f.allocate_person("Anna B.", "2A")
    f.allocate_person("Ewa F.", "2D")
    f.allocate_person("Marcin M.", "4C")
    f.relocate_person("2A", "12B")
    f.relocate_person("2D", "13B")
    f.relocate_person("4C", "12C")
    # print(f.time)
    # print(f.get_day())
    # print(f.get_hour())
    # print(f.get_movie())
    pprint(f.seats)
    print(f.get_empty_seats())
    ticket_printer("Anna Kowalska", "5B", "The Green Mile", "SAT12")
    f.print_tickets(ticket_printer)

buy_a_ticket()
