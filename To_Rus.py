import random

def main():
	eng_text = open(input("File: "), "r", encoding="utf-8").read().split('\n')
	print(eng_text)
	for i in range(len(eng_text)):
		sens = eng_text[i].split(' - ')
		print(f"{i}. {sens[0]}")
		input()
		print(sens[1])

if __name__ == "__main__":
	main()