import module1 # import file module1.py

def main():
	print("Module 2 name {}".format(__name__))

if __name__ == '__main__':
	main() # current file method

module1.main() # External method call
