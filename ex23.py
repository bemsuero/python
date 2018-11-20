import sys
script, input_encoding, error = sys.argv

# grabs the file, picks which encoding type we're doing, the type of errors (option default: strict)
def main(language_file, encoding, errors):
# read the line from the file
    line = language_file.readline()
# if the line exists, run function print_line and return this function
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
# takes the line, takes out the \n and spaces. then encode it into utf-8 and decode it into string
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
# print out raw_bytes and cooked_string
    print(raw_bytes, "<==>", cooked_string)
# open the file languages
languages = open("languages.txt", encoding="utf=8")
# run the function with languages file
main(languages, input_encoding, error)

# things I've never seen: input_encoding, readline(), encoding, raw_bytes, cooked_string
