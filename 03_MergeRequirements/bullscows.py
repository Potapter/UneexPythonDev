import random

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


def main():
	print('Вы выиграли! Количество неудачных попыток:' , gameplay(ask, inform, ['abc', 'abb', 'aaa']))
	return
	
if __name__ == '__main__':
	main()
