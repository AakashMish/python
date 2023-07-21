import sys
import argparse

def main():
	#add_using_sysargv()
	add_using_argparse()


def add_using_sysargv():
	n = len(sys.argv)
	value = 0
	if n < 2:
		print ('Pass the numbers as CLA')
	else:
		for i in range(1,n):
			value = value + int(sys.argv[i])
	print ('Addition result ', value)

def add_using_argparse():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--first", help = "First no", required=True)
	parser.add_argument("-s", "--second", help = "Second no", required=True)
	args = parser.parse_args()

	if args.first and args.second:
		print('Addition is ', int(args.first) + int(args.second))
if __name__ == '__main__':
	main()
