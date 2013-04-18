(define euler (lambda (n) (euler2 0 0 n)))

(define euler2 (lambda (x y n) (cond[(or (= x n)
                                         (= y n))
                                     1]
                                    [else (+ (euler2 (+ x 1) y n)
                                             (euler2 x (+ y 1) n))])))