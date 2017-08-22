import Data.Word

solve :: Word32 -> Word32
solve n = ssolve n 0 0

ssolve :: Word32 -> Word32 -> Word32 -> Word32
ssolve 0 m _ = m
ssolve n m m_terms = uncurry (ssolve (n - 1)) (cmp m m_terms n (count n))

cmp :: Word32 -> Word32 -> Word32 -> Word32 -> (Word32, Word32)
cmp a a_count b b_count
    | b_count > a_count = (b, b_count)
    | otherwise = (a, a_count)

count :: Word32 -> Word32
count 1 = 1
count n
    | even n = 1 + count (div n 2)
    | otherwise = 1 + count (3 * n + 1)

main = putStrLn (show (solve 1000000))