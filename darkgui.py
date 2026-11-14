# Art library created by Tellmehey
# more graphics soon.

blinds = "[+]\n"
deltaFrameXXX = 1 / 30
for i in range(300):
    blinds = blinds + "[+]\n"
blood = '''
  /\\ \\
 /  \\ \\
|  * | |
|    | |
 \\__/_/
'''
sword = '''
/\\
\\ \\
 \\ \\/\\
  \\/ /
  / /\\
  \\/\\/
'''
# blood = "  /\ \ \n /  \ \ \n|  * | |\n|    | |\n \__/_/"
# sword ="/\ \n\ \ \n \ \/\ \n  \/ /\n  / /\ \n  \/\/"

def render(a):
    if a == "blood":
        print(blood)
    elif a == "sword":
        print(sword)
