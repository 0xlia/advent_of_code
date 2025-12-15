from itertools import combinations


def toggle(light):
    return "." if light == "#" else "#"

def press_button(lights, button):
    """
    Docstring for press_button
    
    :param lights: [".", "#", "."]
    :param button: list of toggles
    """

    for part in button:
        lights[part] = toggle(lights[part])

    return lights

def main():
    total_button_presses = 0


    with open("input10.txt") as f:
        for line in f.readlines():
            fewest_presses = 0

            # parse line
            line = line.strip().split()
            final_state = [light for light in line[0][1:-1]]
            lights = ["." for light in range(len(final_state))]
            buttons = [[int(part) for part in button[1:-1].split(",")] for button in line[1:-1]]

            print(final_state, lights,  buttons)

            # combine buttons
            # 1 Button 

            for button in buttons:
                if final_state == press_button(lights.copy(), button):
                    print(1, button, press_button(lights.copy(), button))
            
            # 2 Buttons
            for button0, button1 in combinations(buttons,2):
                if final_state == press_button(press_button(lights.copy(), button0), button1):
                    print(2, button0, button1, press_button(press_button(lights.copy(), button0), button1))
                    





if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()