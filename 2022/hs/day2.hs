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

main :: IO ()
main = do
    contents <- readFile "input.txt"
    let linesList = lines contents
    putStrLn "Lines in file:"
    mapM_ putStrLn linesList
