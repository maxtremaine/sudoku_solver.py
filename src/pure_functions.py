def get_missing_digits(ls: list[int]) -> list[int]:
	return [ x for x in range(1, 10) if x not in ls ]