-- A Rock
-- B Paper
-- C Scissors

import System.IO
data RPS = Rock | Paper | Scissors deriving (Eq, Ord) 

plyIn :: Char -> RPS
plyIn 'A' =  Rock
plyIn 'B' =  Paper
plyIn 'C' =  Scissors
plyIn 'X' =  Rock
plyIn 'Y' =  Paper 
plyIn 'Z' =  Scissors

score :: RPS -> Int
score Rock      = 1
score Paper     = 2
score Scissors  = 3

battle:: RPS -> RPS -> Int
-- battle  ply1 ply2 
battle Rock Paper       = 6 
battle Paper Scissors   = 6 
battle Scissors Rock    = 6 
battle Paper Rock       = 0 
battle Rock Scissors    = 0 
battle Scissors Paper   = 0 
battle _ _   = 3 


transList :: (Char,Char) -> (RPS, RPS)
transList (a,b) = (plyIn a, plyIn b) 


elfList = [('A','Y'), ('B','X'), ('C', 'Z')]


movesList  = map transList elfList 

faa (a,b) = score b + (battle a b)
scoreList = sum $ map faa movesList



readLines :: FilePath -> IO [String]
readLines filePath = do
    handle <- openFile filePath ReadMode
    contents <- hGetContents handle
    let linesOfFile = lines contents
    hClose handle
    return linesOfFile

readInput :: FilePath -> IO [(RPS, RPS)]
readInput fn = (map parseLine . lines ) <$> readFile fn
  where parseLine (c1:' ':c2:[]) = transList (c1,c2)


-- main:: IO()
-- main = readInput "input.txt" 

-- main:: IO()
-- main = do
--   linesOfFile <- readLines "input.txt"
--   print linesOfFile

bubbleSort [] = []
bubbleSort [x] = [x]
bubbleSort (x:y:xs) = if x>y
                        then y : bubbleSort (x:xs)
                        else x : bubbleSort (y:xs)

rr:: Int->Int->[Int]
rr a b  =  if a < b
                then [] 
                else a : rr (a-1) b 

revL :: Int -> Int -> [Int]
revL a b 
    | a < b = []
    | otherwise = a : revL (a-1) b 



maxInList :: [Int] -> Int
maxInList [] = 0 
maxInList [x] = x 
maxInList (x:xs) = if x > maxTail then x else maxTail
            where maxTail = maxInList xs

rev [] = [] 
rev (x:xs) =  (rev xs) ++ [x]

rev' :: [a] -> [a]
rev' xs = neki xs [] 
    where neki [] acc = acc
          neki (x:xs) acc = neki xs (x:acc)



rev'' :: [Int] -> [Int]
rev'' ll = llrev ll []
    where llrev [] acc = acc 
          llrev (x:xs) acc = llrev xs (x:acc)

takeS :: [Int] -> [Int]
takeS [] = []
takeS [x] = []
takeS (x:y:xs) = y : takeS xs


tN :: [a] -> [a]
tN [] = []
tN ll = go ll 1 
    where go [] _ = []
          go (x:xs) n 
            | n == 10 = x : go xs 1
            | otherwise = go xs (n+1)

-- skipN :: [a]-> a -> [a]
skipN [] _ = []
skipN ll n = go ll n 0 where
    go  xs 0 i = xs
    go (x:xs) n i = if i `mod` n == 0 then x : go xs n (i+1)  else go xs n i 

con :: [a] -> [a] -> [a]
con [] [] = []
con [] xs = xs
con xs [] = xs
con (x:xs) ll  = x : con xs ll   -- : h : con (x:xs) (t)  







--
--
-- main :: IO ()
-- main = do
--     contents <- readFile "input.txt"
--     let linesList = lines contents
--     putStrLn "Lines in file:"
--     mapM_ putStrLn linesList
