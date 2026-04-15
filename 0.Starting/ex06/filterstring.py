from ft_filter import ft_filter
import argparse


def check_length(item, number):
    """Function check_length uses a lamda to verify
if the length is greater than the number provided"""
    return (lambda word: len(word) > number)(item)


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

        filtered = ft_filter(check_length, string, number)

        print(f"{filtered}")

    except (ValueError, AssertionError) as e:
        print("AssertionError:", e)
