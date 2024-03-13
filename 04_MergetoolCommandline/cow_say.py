import cmd
import shlex
import cowsay

COWSAY_PRESET = ["'Hello, World!'", "'Oh, hi Mark'", "'Cows will take over the world'", "Blabla"]

class numbername(cmd.Cmd):
    prompt = "cmd>> "

    def do_cowsay(self, line):
        """Draws a cow saying a message. Required parameter: message, optional positioned pparameters: cow, eyes, tongue."""
        args = shlex.split(line)
        args = {'message': args[0], 'cow': 'default' if len(args) < 2 else args[1],
                    'eyes': 'oo' if len(args) < 3 else args[2], 'tongue': '  ' if len(args) < 4 else args[3]}
        print(cowsay.cowsay(**args))

    def do_list_cows(self, line):
        """Prints a list of cows in a directory. Required parameter: directory."""
        print(cowsay.list_cows(line))
    
    def do_make_bubble(self, line):
        """Draws a bubble with text. Required parameter: message."""
        print(cowsay.make_bubble(line))
    
    def do_cowthink(self, line):
        """Draws a cow thinking about a message. Required parameter: message, optional positioned pparameters: cow, eyes, tongue."""
        args = shlex.split(line)
        args = {'message': args[0], 'cow': 'default' if len(args) < 2 else args[1],
                    'eyes': 'oo' if len(args) < 3 else args[2], 'tongue': '  ' if len(args) < 4 else args[3]}
        print(cowsay.cowthink(**args))

    def complete_cowsay(self, text, line, begidx, endidx):
        words = (line[:endidx] + ".").split()
        DICT = []
        match len(words):
            case 2:
                match words[0]:
                    case 'cowsay':
                        DICT = COWSAY_PRESET
                    case 'cowthink':
                        DICT = COWTHINK_PRESET
            case 3:
                if words[0] == 'cowsay' or words[0] == 'cowthink':
                    DICT = ['default', 'kitten']
            case 4:
                if words[0] == 'cowsay' or words[0] == 'cowthink':
                    DICT = ['oo', '^^', 'Oo']
            case 5:
                if words[0] == 'cowsay' or words[0] == 'cowthink':
                    DICT = ["'  '", '^^']

        return [c for c in DICT if c.startswith(text)]


if __name__ == '__main__':
    numbername().cmdloop() 
