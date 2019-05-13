def factors():
	for j in range(2,100):
		a = [i for i in range(1, j//2 + 1) if not j%i] + [j]
		if len(a)>=9:
			return(a)

if __name__ == '__main__':
    print(factors())
