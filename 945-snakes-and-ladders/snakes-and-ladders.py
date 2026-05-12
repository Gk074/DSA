class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        target = n * n

        def get_position(square):
            row_from_bottom = (square - 1) // n
            col = (square - 1) % n

            row = n - 1 - row_from_bottom

            if row_from_bottom % 2 == 1:
                col = n - 1 - col

            return row, col

        q = deque()
        q.append((1, 0))   # square, moves

        visited = set()
        visited.add(1)

        while q:
            square, moves = q.popleft()

            if square == target:
                return moves

            for next_square in range(square + 1, min(square + 6, target) + 1):
                r, c = get_position(next_square)

                if board[r][c] != -1:
                    final_square = board[r][c]
                else:
                    final_square = next_square

                if final_square not in visited:
                    visited.add(final_square)
                    q.append((final_square, moves + 1))

        return -1