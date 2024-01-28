import random
import webbrowser
import os
import pyautogui
import time
import wikipedia

GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"
OTHER = "\033[33m"

responses1 = ["Hi", "Hello", "hi", "hello", "How can I help you?"]
responses2 = ["Bye", "Goodbye", "Goodbye", "Bye"]
responses3 = ["How are you?", "how are you?", "how are you", "How Are You", "How Are You?", "How are you"]
search = ["Search", "search", "SEARCH"]
exit = ["exit", "Exit", "EXIT"]
game = ["game", "Game", "GAME", "start game", "Start Game", "start Game", "start Game"]
terminal = ["terminal", "Terminal", "TREMINAL"]
user = ["fine", "Fine", "FINE"]
ls = ["ls"]

random_number = random.randint(1, 125)

def response1():
    return random.choice(responses1)
def response2():
    return random.choice(responses2)

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open_new_tab(url)

m = input(OTHER + "Enter your namme:" + RESET)
print(f"{GREEN}Welcome Back! {m}{RESET}")
AI = "Max"
y = RED + ": " + RESET
you = RED + "(You)" + RESET
ai = RED + "(AI)" + RESET




def mainTasK():
    while (True):
        i = input(m+you+y).lower()
        if i in (responses1):
           print (AI + ai + y + response1() +" " + m)
    
        elif i in (search):
            s = input("What do you want to search on google?:")
            search_google(s)
        
        elif i in (ls):
            print("terminal\nsearch\nexit\ngame")
    
        elif i in (game):
    
            print("Starting game")
            # game starting
            import random
            
            board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            
            def display_board():
                print(board[0] + "|" + board[1] + "|" + board[2])
                print("-+-+-")
                print(board[3] + "|" + board[4] + "|" + board[5])
                print("-+-+-")
                print(board[6] + "|" + board[7] + "|" + board[8])
            
            def check_win(player):
                return ((board[0] == player and board[1] == player and board[2] == player) or
                        (board[3] == player and board[4] == player and board[5] == player) or
                        (board[6] == player and board[7] == player and board[8] == player) or
                        (board[0] == player and board[3] == player and board[6] == player) or
                        (board[1] == player and board[4] == player and board[7] == player) or
                        (board[2] == player and board[5] == player and board[8] == player) or
                        (board[0] == player and board[4] == player and board[8] == player) or
                        (board[2] == player and board[4] == player and board[6] == player))
            
            def player_move():
                while True:
                    try:
                        move = int(input("Enter your move (1-9): "))
                        if board[move-1] == " ":
                            board[move-1] = "X"
                            break
                        else:
                            print(RED + "That space is already taken. Try again." + RESET)
                    except ValueError:
                        print(RED + "Invalid input. Try again." + RESET)
            
            def ai_move():
                move = None
                for i in range(1, 10):
                    if board[i-1] == " ":
                        board[i-1] = "O"
                        if check_win("O"):
                            move = i
                            break
                        board[i-1] = " "
                if move is None:
                    for i in range(1, 10):
                        if board[i-1] == " ":
                            board[i-1] = "X"
                            if check_win("X"):
                                move = i
                                break
                            board[i-1] = " "
                if move is None:
                    while True:
                        move = random.randint(1, 9)
                        if board[move-1] == " ":
                            break
                board[move-1] = "O"
            
            while True:
                board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
                display_board()
                while True:
                    player_move()
                    display_board()
                    if check_win("X"):
                        print(GREEN + "You won!" + RESET)
                        break
                    if " " not in board:
                        print("It's a tie!")
                        break
                    ai_move()
                    display_board()
                    if check_win("O"):
                        print(RED + "You lost!" + RESET)
                        break
                play_again = input("Do you want to play again? (y/n) ")
                if play_again.lower() != "y":
                    break
        #game ending
        elif i in (terminal):
            #terminal start
            print(RED + "Starting Terminal" + RESET)
            import subprocess
            
            while True:
                cmd = input('$ ')
                if cmd.lower() == 'exit':
                    break
                try:
                    result = subprocess.run(cmd.split(), capture_output=True, text=True)
                    print(result.stdout.strip())
                    if result.stderr:
                        print(result.stderr.strip())
                except FileNotFoundError:
                    print(f'{cmd}: command not found')
        #terminal end
    
        elif i in (responses3):
            print("I am fine " + m)
            fine = input("And you " + m + y)
            if i in (user):
                print("I am happy to hear it :)")
            else:
                print("I am so sorry " + m)
            
        elif i in (responses2):
            print(AI + ai + y + response2() +" " + m)
            break
        elif i in (exit):
            break

        elif 'play music' in i:
            """ Please Change the file path"""
            music_dir = "Music"
            song = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, song[random_number]))

        elif 'open brave' in i:
            brave = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(brave)

        elif 'open instagram' in i:
            webbrowser.open_new_tab("https://www.instagram.com")
        
        elif 'open youtube' in i:
            webbrowser.open_new_tab("https://www.youtube.com")
        
        elif 'open zoro' in i:
            webbrowser.open_new_tab("https://zoro.to/home?source=pwa")
        
        elif 'open google' in i:
            webbrowser.open_new_tab("https://www.google.com")
        
        elif 'open chat gpt' in i:
            webbrowser.open_new_tab("https://chat.openai.com/chat")

        elif 'open cmd' in i:
            time.sleep(2)
            pyautogui.hotkey('win', 'r')
            time.sleep(1)
            pyautogui.press('c')
            pyautogui.press('m')
            pyautogui.press('d')
            pyautogui.hotkey('enter')
        elif 'open vs code' in i:
            """ Please Change the file path"""
            vs_path = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(vs_path)

        elif 'play video' in i:
            """ Please Change the file path"""
            video_path = "Videos"
            video = os.listdir(video_path)
            os.startfile(os.path.join(video_path, video[random_number]))

        elif 'wikipedia' in i:
            print('Searching on wikipedia...')
            quray = i.replace("wikipedia", "")
            results = wikipedia.summary(quray, sentences = 3)
            print("Accoding to wikipedia")
            print(GREEN, results, RESET)        

        else:
            print(AI + ai + y + "Error, command not found :( ")
            yes_no = input("Do you yant to search this on google(Y/n): ")
            if (yes_no=='n' or yes_no=='N'):
                continue
            else:
                search_google(i)


                
if True:
    mainTasK()
