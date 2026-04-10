import argparse

def odd_or_even():
	num = int(args.items[0])

	if num % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")

        
if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		description="Script to determine if the argument given is an odd number or an even number"
        )

	parser.add_argument("items", nargs="*", help="Add one number at a time")
	args = parser.parse_args()

	if len(args.items) != 0:
		try:
			assert len(args.items) == 1, "more than one argument is provided"
            
			try:
				int(args.items[0])
			except ValueError:
				assert False, "argument is not an integer"
			
			odd_or_even()
        
		except (ValueError, AssertionError) as e:
			print("AssertionError:", e)