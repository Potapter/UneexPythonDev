import random
import argparse
import validators
import urllib.request

def bullscows(guess: str, secret: str) -> (int, int):
	bulls = set()
	cows = set()
	d = list(set(guess))
	
	for i in range(len(secret)):
		if secret[i] == guess[i]:
			bulls.add(secret[i])
		if secret[i] in d:
			cows.add(secret[i])

	return len(bulls), len(cows)

def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
	wished = random.choice(words)
	print('Слово загадано!')
	
	attempts = 0
	while (assumption := ask("Введите слово: ", words)) != wished:
		attempts += 1
		inform("Быки: {}, Коровы: {}", *bullscows(assumption, wished))
		print('Неправильно! Попробуй ещё!\n')

	return attempts

def ask(prompt: str, valid: list[str] = None) -> str:
	print(prompt)
	
	if valid != None:
		print('Список слов:', *valid)
		while (word := input()) not in valid:
			print('Я сказал из списка!!!\n' + prompt)
	else:
		word = input() 
	
	return word

def inform(format_string: str, bulls: int, cows: int) -> None:
	print(format_string.format(bulls, cows))
	return

parser = argparse.ArgumentParser('bullscows')
parser.add_argument('-m', '--reference', nargs = 2, metavar = ('dictionary', 'length'), default = ['https://raw.githubusercontent.com/Harrix/Russian-Nouns/main/dist/russian_nouns.txt', 5], help = 'Запускает референс-реализацию игры: в игре учавствуют слов из словаря dictionary (имя файла или URL ссылка) длины length')

args = parser.parse_args()

def main():
	game_dictionary = []
	
	if validators.url(args.reference[0]):
		try:
			req = urllib.request.Request(args.reference[0])
		except Exception as err:
			print("Некорректная ссылка!")
			return

		with urllib.request.urlopen(req) as response:
			for word in response.read().decode('UTF-8').split('\n'):
				if len(word) == int(args.reference[1]):
					game_dictionary.append(word)
	
	else:
		print('path')
	
	print('Вы выиграли! Количество неудачных попыток:' , gameplay(ask, inform, game_dictionary))
	return
	
if __name__ == '__main__':
	main()
