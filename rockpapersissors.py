# A basic rock paper sissors game that can be ran from the terminal
# I am using this to learn git so please bare with me

exit_flag = False
line_count = 100
line_string = "-"

# Main rock paper sissors game that is to be executed repeatly until quited
def mainGameLoop():
    global exit_flag
    player_selection = input("""
    Please select one of the following options:
    \n\t(r)ock,
    \t(p)aper,
    \t(s)issors,
    \t(q)uit\n
    input: """)

    if player_selection == "q":
        exit_flag = True
        return

print(f"""{line_string*line_count}
      
    Welcome to my rock paper sissors game, a simple verision I am using to learn git

{line_string*line_count}
""")

while not exit_flag:
    mainGameLoop()

print(f"""{line_string*line_count}
      
    Thanks for playing!
      
{line_string*line_count}
""")