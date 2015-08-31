import Data.List

solve :: Int -> Int
solve lim = foldr (*) 1 [1]

listFactors :: Int -> [Int]
listFactors lim = concat [(nub (factor a)) | a <- [1..lim]]

factor :: Int -> [Int]
factor x = factor' x 2 []

factor' :: Int -> Int -> [Int] -> [Int]
factor' x d li
	| d >= x = x : li
	| x `mod` d == 0 = factor' (x `div` d ) d (d : li)
	| otherwise = factor' x (d + 1) li

