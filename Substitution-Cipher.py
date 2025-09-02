
custom_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


def Get_Index(i):
    if i in custom_alphabet:
        return custom_alphabet.index(i)
    return "Not In custom_alphabet"

def Shift_Index(text, key_index, inpu):
    shifted_text = ""
    for i in range(len(text)):
        char = text[i]
        char_index = Get_Index(char)
        if char_index == "Not In custom_alphabet":
            shifted_text += char # Any char that is not recognized goes into custom_alphabet as is
            continue

        shift = key_index[i % len(key_index)]

        if inpu == '+':
            new_index = (char_index + shift) % len(custom_alphabet)
        elif inpu == '-':
            new_index = (char_index - shift) % len(custom_alphabet)

        shifted_text += custom_alphabet[new_index]
    return shifted_text

class Cipher:
    def __init__(self, text, key):
        self.text = text
        self.key = key
        self.key_index = self.get_key_index()

    def get_key_index(self):
        key_index = []
        for i in self.key:
            k_i = Get_Index(i)
            if k_i == "Not In custom_alphabet":
                key_index.append(1) # If there is a char from the key that is not recognized, append the default value of 1
                continue
            key_index.append(k_i)

        return key_index

class Caesar_Cipher(Cipher):
    def __init__(self, text, key, inpu):
        super().__init__(text, key)
        self.shifted_text = Shift_Index(self.text, self.key_index, inpu)




def main():
    text = input("Provide text to encrypt or decrypt: ")

    inpu = input("Please provide '+' to encrypt or '-' to decrypt: ").strip()
    if inpu not in ('+', '-'):
        print("!!! ERROR provide '-' to decrypt or '+' to encrypt !!!")
        return
    key = input("Provide your key: ")

    m = Caesar_Cipher(text, key, inpu)

    print(m.shifted_text)

if __name__ == "__main__":
    main()



