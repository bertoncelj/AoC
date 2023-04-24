-- A Rock
-- B Paper
-- C Scissors

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
