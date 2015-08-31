solve :: Int -> Int
solve lim = (sum [b | b <- [1..(lim-1)], b `mod` 3 == 0 || b `mod` 5 == 0])
