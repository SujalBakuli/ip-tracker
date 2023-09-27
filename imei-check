def is_valid_imei(imei):
    # Check if the IMEI is 15 digits long
    if len(imei) != 15:
        return False

    # Check if the IMEI consists of only numeric characters
    if not imei.isdigit():
        return False

    # Calculate the IMEI check digit
    imei_digits = [int(digit) for digit in imei]
    checksum = 0
    for i in range(14):
        if i % 2 == 0:
            double_digit = imei_digits[i] * 2
            checksum += double_digit if double_digit < 10 else double_digit - 9
        else:
            checksum += imei_digits[i]

    # The IMEI is valid if the checksum is a multiple of 10
    return checksum % 10 == 0

# Input IMEI number to check
imei = input("Enter the IMEI number: ")

if is_valid_imei(imei):
    print("Valid IMEI number")
else:
    print("Invalid IMEI number")
