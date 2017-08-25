import Data.Word
import Data.List.Extras.Argmax

solve :: Word32 -> Word32
solve n = argmax l
    where l = map count [1..n]

-- ssolve :: Word32 -> Word32 -> Word32 -> Word32
-- ssolve m _ 0 = m
-- ssolve m m_terms n =
--     let n_terms = count n
--     in if n_terms > m_terms then ssolve n n_terms (n-1)
--                             else ssolve m m_terms (n-1)

count :: Word32 -> Word32
count 1 = 1
count n
    | even n = 1 + count (div n 2)
    | otherwise = 1 + count (3 * n + 1)

main = putStrLn (show (solve 1000000))
-- module Main where
-- import Data.List
-- import Data.Maybe

-- f :: Integer -> Integer
-- f n | even n    = n `div` 2
--     | otherwise = 3 * n + 1

-- fs :: Integer -> [Integer]
-- fs 1 = [1]
-- fs n = n : fs (f n)

-- main = print ((fromMaybe 0 (elemIndex (maximum x) x)) + 1)
--     where x = map (length . fs) [1..999999]