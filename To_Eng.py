import random

def main():
	eng_text = open(input("File: "), "r", encoding="utf-8").read().split('\n')
	random.shuffle(eng_text)
	for i in range(len(eng_text)):
		sens = eng_text[i].split(' - ')
		print(sens[1])
		input()
		print(sens[0])

if __name__ == "__main__":
	main()