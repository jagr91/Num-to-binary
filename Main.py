def num_to_bin(number):
    n = 0
    bin_list = []

    try:
        while 2 ** n <= number:
            bin_list.insert(0, 2 ** n)
            n += 1

        binary_number = f'Binary of the number {number} is '

        for n in bin_list:
            if number >= n:
                number -= n
                binary_number += '1'
            else:
                binary_number += '0'

        print(binary_number)
    except SyntaxError:
        print('Wrong input. You need to put an integer')


num_to_bin(1000)
