alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def setCode(message,shift,method):
  setMessage = '' 
  for letter in message:
    if letter in alphabet:
      position = alphabet.index(letter)
  

    if method == "encode":
      newpostion = position + shift
    elif method == "dencode":
      newpostion = position - shift
    else:
      return "Error"
    if letter in alphabet: 
      msg = alphabet[newpostion]
    else:
      msg = letter            
    setMessage += msg

  print(setMessage)


should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'dencode' to decrypt:\n")
  message = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  setCode(message,shift,direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")




