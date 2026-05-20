# Run ty on this

# a = 5
# b = "bla"
# a + b

# No hints, no problems!
def splitter_unhinted(s):
    return s.split()


# No return typing != None! Be explicit
def splitter_no_return_hint(s: str):
    return s.split()


def proper_splitter(s: str) -> list:
    return s.split()


def splitter_bad_return_hint(s: str) -> float:
    return s.split()


def splitter_bad_input_hint(s: int) -> list:
    return s.split()
