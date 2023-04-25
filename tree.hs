{-
      5
     / \
    4  3
   |  / \
  10 3  2

-}

data BinaryTree a = 
  Empty 
  | Node (BinaryTree a) a (BinaryTree a)
  | Leaf a
  deriving (Show, Eq)



treeMap::(a->b)-> BinaryTree a -> BinaryTree b
treeMap _ Empty = Empty
treeMap f (Leaf a) = Leaf (f a)
treeMap f (Node left a right) = Node (treeMap f left) (f a) (treeMap f right)

pre:: BinaryTree a -> [a]
pre Empty = []
pre (Leaf a) = [a]
pre (Node l a r) = [a] ++ pre l ++ pre r 

solve:: [Int] -> [Int] -> Int
readIntList :: IO[Int]
readIntList = do line <- getLine
              return $ map read $ words line

main = do [n, m] <- readIntList
