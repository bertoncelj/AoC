input = [[1000,2000,3000],[4000],[5000,6000],[7000,8000,9000],[10000]]



suml::[Int]->Int
suml [] = 0
suml [x] = x
suml (x:xs) = x + suml xs

get_max::[Int] -> Int
get_max [] = error "empty list" 
get_max [x] = x
get_max (x:xs)
    | x > maxTail = x
    | otherwise = maxTail
    where maxTail = get_max xs



fun x = suml x
sum_list = map fun input
result_day_1 = get_max sum_list
