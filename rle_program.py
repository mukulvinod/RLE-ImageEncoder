from console_gfx import ConsoleGfx

def to_hex_string(data):
    hexy = ""
    for i in data:
        hexx = hex(i)[2:]
        hexy += hexx
    return hexy

#converts between hexes and strings

def count_runs(flat_data):
    count = 0
    run = None
    num = 0

    run = flat_data[0]
    for i in flat_data[1:]:
        if i == run:
            if num == 15:
                count += 1
                num = 0
            num += 1
        else:
            run = i
            count += 1
            num = 0

    count += 1
    return count
#counts the unique runs

def encode_rle(flat_data):
    rle = []
    run = flat_data[0]
    len = 1

    for i in flat_data[1:]:
        if i == run:
            if len == 15:
                rle.extend([len, run])
                len = 0
            len += 1
        else:
            if run is not None:
                rle.extend([len, run])
            run = i
            len = 1
    rle.extend([len, run])

    return rle

def get_decoded_length(rle_data):
    size = sum(rle_data[::2])
    return size

def decode_rle(rle_data):
    data = []
    for i in range(0, len(rle_data), 2):
        lent = rle_data[i]
        val = rle_data[i + 1]
        data.extend([val] * lent)
    return data

def string_to_data(data_string):
    return [int(char, 16) for char in data_string]

def to_rle_string(rle_data):
    str = ""
    i = 0
    while i < len(rle_data):
        leng = rle_data[i]
        val = rle_data[i + 1]
        if leng < 10:
            temp = f"{leng:02d}{val:01x}:"
            temp = temp[1:]
            str += temp
        else:


            str += f"{leng:02d}{val:01x}:"
        i += 2
    return str.rstrip(':')

def string_to_rle(rle_string):
    data = []
    str = rle_string.split(':')

    for i in str:
        leng = int(i[0:-1])
        val = int(i[-1], 16)
        data.extend([leng, val])
    return data
def menu():
    print("RLE Menu")
    print("--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data")
    #menu function eases use of it
def main():
    print("Welcome to the RLE image encoder!")
    print("Displaying Spectrum Image:")
    rainbow = ConsoleGfx.test_rainbow
    ConsoleGfx.display_image(rainbow)
    menu()
    op = int(input("Select a Menu Option: "))
    cond = True
    data = None
    while cond:
        #this is the exit statement
        if op == 0:
            break
        elif op == 1:
            filename = input("Enter name of file to load: ")
            filedata = ConsoleGfx.load_file(filename)
            menu()
            op = int(input("Select a Menu Option: "))
        elif op ==2:
            print("Test image data loaded.")
            #loads the test image
            filedata = ConsoleGfx.test_image
            menu()
            op = int(input("Select a Menu Option: "))
        elif op == 3:
            str = input("Enter an RLE string to be decoded: ")
            rle = string_to_rle(str)
            data = decode_rle(rle)
            #decodes rle string
            menu()
            op = int(input("Select a Menu Option: "))
        elif op == 4:
            str = input("Enter the hex string holding RLE data: ")
            hex = string_to_data(str)
            data = decode_rle(hex)
            menu()
            op = int(input("Select a Menu Option: "))
        elif op == 5:
            str = input("Enter the hex string holding flat data: ")
            data = string_to_data(str)
            menu()
            op = int(input("Select a Menu Option: "))
        #prints the image
        elif op == 6:
            print("Displaying image...")
            ConsoleGfx.display_image(filedata)
            cond = False
            #turns condition into false, ending loop
        elif op == 7:
            rle = encode_rle(data)
            str = to_rle_string(rle)
            print(f'RLE representation: {str}')
            menu()
            op = int(input("Select a Menu Option: "))
        elif op == 8:
            rle = encode_rle(data)
            hex = to_hex_string(rle)
            print(f'RLE hex values: {hex}')
            menu()
            op = int(input("Select a Menu Option: "))
        elif op == 9:
            #flat hex values
            flat = to_hex_string(data)
            print(f'Flat hex values: {flat}')
            menu()
            op = int(input("Select a Menu Option: "))
        else:
            #only executes when number other than 0-9 is inputted
            print("Error! Invalid input.")
            menu()
            op = int(input("Select a Menu Option: "))

#actaully executes main
if __name__ == '__main__':
    main()
