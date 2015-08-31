solve :: Int -> Int
solve x = ssolve x 2

ssolve :: Int -> Int -> Int
ssolve x d  
	| d >= x = x
	| x `mod` d == 0 = ssolve (x `div` d) d
	| otherwise = ssolve x (d + 1)


factor :: Int -> [Int]
factor x = factor' x 2 []

factor' :: Int -> Int -> [Int] -> [Int]
factor' x d li
	| d >= x = x : li
	| x `mod` d == 0 = factor' (x `div` d ) d (d : li)
	| otherwise = factor' x (d + 1) li
