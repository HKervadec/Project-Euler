main = putStrLn (show (solve 100 999))

solve :: Int -> Int -> Int
solve lb lh = maximum (filter palindrome [a*b | a <- [lh,lh-1..lb], b <- [lh,lh-1..a]])


palindrome :: Int -> Bool
palindrome x = (reverse li) == li
	where li = toList x


toList :: Int -> [Int]
toList x
	| x < 10 = [x]
	| otherwise = (mod x 10) : toList (div x 10)
