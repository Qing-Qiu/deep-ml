def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    m = len(a)
    if m == 0:
        return -1
    n = len(a[0])
    if n == 0:
        return -1
    res = []
    for i in range(0, n):
        ans = []
        for j in range(0, m):
            ans.append(a[j][i])
        res.append(ans)
    return res
    