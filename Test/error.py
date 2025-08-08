x = 0
while True:
    try:
        filename = input("Enter filename: ")
        with open(filename) as f:
            f_data = f.read()
    except FileNotFoundError as e:
        print(f"Sorry {filename} doesnt exist")
    else:
        print(f_data)
        x = 0
        break
    finally:
        x += 1
        if x == 3:
            print('Please check file and rerun')
            break

