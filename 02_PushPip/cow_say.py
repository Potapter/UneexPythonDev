import argparse
import cowsay
import sys
import os

parser = argparse.ArgumentParser('cow_say')

parser.add_argument('-n', action='store_true', help = 'If it is specified, the given message will not be word-wrapped')
parser.add_argument('-W', dest='columns', type=int, help = 'Specifies roughly (where the message should be wrapped')
parser.add_argument('-b', action='store_true', help = 'Borg mode')
parser.add_argument('-d', action='store_true', help = 'Causes the cow to appear dead')
parser.add_argument('-g', action='store_true', help = 'Greedy mode')
parser.add_argument('-p', action='store_true', help = 'State of paranoia to come over the cow')
parser.add_argument('-s', action='store_true', help = 'Makes the cow appear thoroughly stoned')
parser.add_argument('-t', action='store_true', help = 'Yields a tired cow')
parser.add_argument('-w', action='store_true', help = 'Yields a rested cow')
parser.add_argument('-y', action='store_true', help = "Brings on the cow's youthful appearance")
parser.add_argument('-e', dest='eye_string', type=str, help = "Change cow's eyes with first two letters of given string")
parser.add_argument('-T', dest = 'tongue_string', type=str, help = "Change cow's eyes with letters in given string of length 2")
parser.add_argument('-f', action='store_true', help = 'Specifies a particular cow picture file (''cowfile'') to use')
parser.add_argument('-l', action='store_true', help = 'Show list all cowfiles on the current COWPATH')

args = parser.parse_args()


def main():
	if args.l:
		path = os.environ.get("COWPATH", cowsay.COW_PEN)
		print(cowsay.list_cows(path))
		return

	message = sys.stdin.read()
	print(cowsay.cowsay(message, **vars(args)))
	return
	
if __name__ == '__main__':
	main()
