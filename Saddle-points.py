def saddle_points(matrix):

    """Saddle points exercise. 
    Detect saddle points in a matrix, being the point on a surface at which the height is maximum in one direction and minimum in another (for example, in the perpendicular direction).

    Parameters: matrix - provides the data as grids that show the heights of the trees. The rows of the grid represent the east-west direction, and the columns represent the north-south direction.
    
    Returns:
    candidates - list of dictionary with the position in the matrix of the candidate tree"""
    
    if not matrix:
        return []  # Return empty list
    
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