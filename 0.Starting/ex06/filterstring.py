from ft_filter import ft_filter
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script that filters strings \
            based on the length of the words"
    )
    parser.add_argument("items", nargs="*",
                        help="text to be analysed and word size")
    args = parser.parse_args()

    try:
        assert len(args.items) == 2, "the arguments are bad"

        try:
            number = int(args.items[1])
        except ValueError:
            assert False, "the arguments are bad"

        # "one two three!" will trigger shell expansion failed error.
        #    use 'one two three!' to get the right error
        string = args.items[0]
        if not all(char.isalpha() or char.isspace() for char in string):
            raise AssertionError("the arguments are bad")

        # list comprehension expression:
        #    what to produce + where to get the items + optional filtering
        # lambda = small anonymous expression: [lambda arguments: expression]
        filtered = list(ft_filter(lambda word: len(word) > number,
                                  string.split()))

        print(f"{filtered}")

    except (ValueError, AssertionError) as e:
        print("AssertionError:", e)
