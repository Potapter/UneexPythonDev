import cmd
import shlex
import cowsay

COWSAY_PRESET = ["'Hello, World!'", "'Oh, hi Mark'", "'Cows will take over the world'", "Blabla"]

class numbername(cmd.Cmd):
    prompt = "cmd>> "

    def do_cowsay(self, line):
        args = shlex.split(line)
        args = {'message': args[0], 'cow': 'default' if len(args) < 2 else args[1],
                    'eyes': 'oo' if len(args) < 3 else args[2], 'tongue': '  ' if len(args) < 4 else args[3]}
        print(cowsay.cowsay(**args))

    def do_list_cows(self, line):
        pass
    
    def do_make_bubble(self, line):
        pass
    
    def do_cowthink(self, line):
        pass

    def complete_cowsay(self, text, line, begidx, endidx):
        words = (line[:endidx] + ".").split()
        DICT = []
        match len(words):
            case 2:
                match words[0]:
                    case 'cowsay':
                        DICT = COWSAY_PRESET

        return [c for c in DICT if c.startswith(text)]


if __name__ == '__main__':
    numbername().cmdloop() 
