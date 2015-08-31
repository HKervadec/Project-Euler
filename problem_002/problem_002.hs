solve :: Int -> Int
solve lim = (sum (takeWhile (< lim) (filter even (fibo 0 1))))

fibo :: Int -> Int -> [Int]
fibo a b = a : (fibo b (a+b))
