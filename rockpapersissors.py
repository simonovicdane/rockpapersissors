# A basic rock paper sissors game that can be ran from the terminal
# I am using this to learn git so please bare with me

exit_flag = False
line_count = 100
line_string = "-"

def mainGameLoop():
    print("hello")
    print("fart")
    global exit_flag
    exit_flag = True


print(f"""{line_string*line_count}
      
    Welcome to my rock paper sissors game, a simple verision I am using to learn git

{line_string*line_count}""")

while not exit_flag:
    mainGameLoop()

print(f"""{line_string*line_count}
      
    Thanks for playing!
      
{line_string*line_count} """)