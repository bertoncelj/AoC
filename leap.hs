import Text.Printf 
leapDay:: Int -> String
leapDay year = "12.09." ++ show year

normDay:: Int -> String
normDay year = "13.09." ++ show year

julian :: Int -> String
julian year
  | year `mod` 4 == 0 = leapDay year
  | otherwise         = normDay year


gregorian:: Int -> String
gregorian year 
  | year `mod` 400 == 0 = leapDay year
  | year `mod` 4 == 0 && ( year `mod` 100 /= 0) = leapDay year
  | otherwise = normDay year 


russia:: Int -> String
russia year
 | year <= 1917 = julian year
 | year == 1918 = "26.09.1918"
 | otherwise =  gregorian year


 
