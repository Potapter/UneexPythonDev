import argparse
import cowsay

parser = argparse.ArgumentParser("cow_say")

parser.add_argument("-l", action="store_true")

args = parser.parse_args()

def main():
	print(args)

if __name__ == '__main__':
	main()
