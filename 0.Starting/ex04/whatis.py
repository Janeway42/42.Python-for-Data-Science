import argparse

def odd_or_even():
    num = int(args.items[0])

    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="Script that scrapes images from a given website"
        )

    parser.add_argument("items", nargs="*", help="images to read metadata from")
    args = parser.parse_args()

    if len(args.items) != 0:
        try:
            assert len(args.items) == 1, "more than one argument is provided"
            odd_or_even()
        except (ValueError, AssertionError) as e:
            print("AssertionError:", e)
        