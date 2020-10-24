import string


def add_one_binary(value):
    for i in range(1, len(value) + 1):
        if(value[-i] == "1"):
            value[-i] = "0"

        else:
            value[-i] = "1"
            return(value)


# It is important to know how long the binary string need to be to encode every character.
# I assumed that the minimum viable binary string length would be where 2^i > n characters
def gen_bin_len(inList):
    i = 0
    while(2**i < len(inList)):
        i += 1

    return(i)


def gen_encoder(inList):
    i = gen_bin_len(inList)
    first_value = "0" * i  # Make a string n length of i, ie "00000" if i is 5

    # Base Case
    encoder = {inList[0]: first_value}
    inList.remove(inList[0])

    # current_binary set to the value of the next binary, ie a = 00 and b = 01
    current_binary = first_value
    for value in inList:
        current_binary = add_one_binary(list(current_binary))
        encoder.update({value: "".join(current_binary)})

    return(encoder)


# Inverts the encoder
def gen_decoder(inDict):
    return(dict(zip(inDict.values(), inDict.keys())))


# String in python are immutable, so they hard to be converted to lists and back
def main():
    encoder = gen_encoder(list(string.printable))
    decoder = gen_decoder(encoder)

    encoded = []
    demo_string = "Hello World!"
    for char in demo_string:
        encoded.append(encoder[char])

    decoded = []
    for code in encoded:
        decoded.append(decoder[code])

    print(encoded)
    print("".join(decoded))


if __name__ == "__main__":
    main()
