import Data.List

-- input data 
neki :: [Int]
neki = [10,20,10,20,30]

sorted_groups :: [Int] -> [[Int]]
sorted_groups x =  group . sort $ x

find_pairs::[Int] -> Int
find_pairs x =  length x `div` 2

final:: Int
final = sum . map find_pairs $ sorted_groups  neki 


main :: IO()
main = undefined

