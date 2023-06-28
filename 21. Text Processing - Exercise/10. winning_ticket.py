def valid_ticket_check(ticket):
    if len(ticket) == 20:
        return True
    return False


def winning_ticket_check(ticket):
    winning_symbols = ['@', '#', '$', '^']
    for current_symbol in winning_symbols:
        for number_of_symbols in range(10, 5, -1):
            number_of_repetitions = number_of_symbols * current_symbol
            if number_of_repetitions in ticket[:10] and number_of_repetitions in ticket[10:]:
                if number_of_symbols == 10:
                    return f'ticket "{ticket}" - {number_of_symbols}{current_symbol} Jackpot!'
                return f'ticket "{ticket}" - {number_of_symbols}{current_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = input().split(", ")

for current_ticket in tickets:
    stripped_ticket = current_ticket.strip()
    if valid_ticket_check(stripped_ticket):
        print(winning_ticket_check(stripped_ticket))
    else:
        print("invalid ticket")
