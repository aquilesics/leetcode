var countSquares = function (matrix) {
    let count = 0
    let n = matrix.length
    let m = matrix[1].length

    for (var i = 1; i < n; i++) {
        for (var j = 1; j < m; j++) {

            if (matrix[i][j] === 0) {
                console.log("")
            } else {
                matrix[i][j] = Math.min(Math.min(matrix[i - 1][j], matrix[i][j - 1]), matrix[i - 1][j - 1]) + 1;
            }
        }



    }

    for (var i = 0; i < n; i++) {
        for (var j = 0; j < m; j++) {
            count += matrix[i][j]
        }

    }
    return count
}
