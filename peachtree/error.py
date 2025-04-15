x = 0
while True:

    try:
        filename = input(f"Which file would you like to open?:")
        with open(filename, "r") as fh:
            fh_data = fh.read()
    except FileNotFoundError:
        print(f"Sorry {filename} can't be found")
    else:
        print(fh_data)
        x = 0
        break
    finally:
        x += 1
        if x == 3:
            print(f"Please check file and rerun")
            break
