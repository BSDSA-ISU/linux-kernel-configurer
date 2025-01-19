import curses

def menu(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLUE)  
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  
    curses.curs_set(0)
    options = ["Option 1", "Option 2", "Option 3", "Exit"]
    current_row = 0

    exter = True

    while exter:
        stdscr.clear()
        for idx, option in enumerate(options):
            if idx == current_row:
                stdscr.addstr(idx, 0, option, curses.color_pair(1))
            else:
                stdscr.addstr(idx, 0, option)

        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(options) - 1:
            current_row += 1
        elif key == ord("\n"):
            if options[current_row] == "Exit":
                break
            stdscr.addstr(len(options) + 1, 0, f"You selected: {options[current_row]}")
            exter = False
          #  stdscr.refresh()
         #   stdscr.getch()

    stdscr.refresh()
    return f"{option[current_row]}"

e = curses.wrapper(menu)
print(e)