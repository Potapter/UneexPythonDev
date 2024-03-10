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
	pass
	return

def ask(prompt: str, valid: list[str] = None) -> str:
	pass
	return

def inform(format_string: str, bulls: int, cows: int) -> None:
	pass
	return


def main():
	print(bullscows('ропот', 'полип'))
	return
	
if __name__ == '__main__':
	main()
