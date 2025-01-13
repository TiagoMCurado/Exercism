def saddle_points(matrix):

    """Returns the reversed String.
    

    #Parameters:
    #    str1 (str):The string which is to be reversed.

    #Returns:
    #    reverse(str1):The string which gets reversed.List of dictionary com os valores da linha e coluna da arvore candidata"""
    
    if not matrix:
        return []  # Return empty matrix
    first_row_length = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_length:
            raise ValueError("irregular matrix")

    candidates = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for i in range(num_rows):
        for j in range(num_cols):
            tree = matrix[i][j]
            
            if tree != max(matrix[i]):
                continue
                
            col_values = []
            for row in range(num_rows):
                col_values.append(matrix[row][j])
                
            if tree != min(col_values):
                continue
            
            candidates.append({"row":i+1,"column":j+1})

    return candidates