_wincpy_ start 8c2e6882503c4baa9ce2e050497c3f2fPYTEST

import sys

def filter_stdin(char):
    text = sys.stdin.read() # read stdin
    n_chars_removed = text.count(char) # count char in stdin
    text = text.replace(char, '') # remove char from stdin
    sys.stdout.write(text) # write to stdout
    sys.stderr.write(str(n_chars_removed)) # write to stderr
    
if __name__ == "__main__":
    if len(sys.argv) < 2: # check for argument
        print("Please provide character to remove from stdin.")
    else:
        char = sys.argv[1] # get character to remove from argument
        filter_stdin(char)