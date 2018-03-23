def columns(matrix):
	''' extracts a list of columns from the matrix '''
	cols = []
	for i in range(len(matrix)):
		cols.append([row[i] for row in matrix])
	print(cols)

def search_hori(matrix):
	for row in matrix:
		if has_digit_sequence(row):
			return True
	return False


columns([[1, 2, 1, 1],
              [1, 1, 4, 1],
              [1, 3, 1, 6],
              [1, 7, 2, 5]])
