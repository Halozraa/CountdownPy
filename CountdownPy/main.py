import time


    
def print_red(text):
    red_color = "\033[91m"
    reset_color = "\033[0m"
    print(red_color + text + reset_color)
        
def print_green(text):
    green_color = "\033[92m"
    reset_color = "\033[0m"
    print(green_color + text + reset_color)

def print_yellow(text):
    yellow_color = "\033[93m"
    reset_color = "\033[0m"
    print(yellow_color + text + reset_color)

def countdown(seconds):
    while seconds > 0:
        if seconds <= 3:
            print_red(f"{seconds}")
        elif seconds <= 6:
            print_yellow(f"{seconds}")
        elif seconds >=7 :
            print_green(f"{seconds}")
        time.sleep(1) # menghitung mundur
        seconds -= 1
    print_red(f"Program berakhir")

def main():
    try:
        seconds = int(input("Masukan jumlah waktu untuk dihitung mundur: "))
        countdown(seconds)
    except ValueError:
        print("Masukan angka bukan huruf")


if __name__=='__main__':
    main()
    
