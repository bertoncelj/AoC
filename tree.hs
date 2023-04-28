{-
      5
     / \
    4  3
   |  / \
  10 3  2

-}

data BinaryTree a
  = Empty
  | Node (BinaryTree a) a (BinaryTree a)
  | Leaf a
  deriving (Show, Eq)

treeMap :: (a -> b) -> BinaryTree a -> BinaryTree b
treeMap _ Empty = Empty
treeMap f (Leaf a) = Leaf (f a)
treeMap f (Node left a right) = Node (treeMap f left) (f a) (treeMap f right)

pre :: BinaryTree a -> [a]
pre Empty = []
pre (Leaf a) = [a]
pre (Node l a r) = [a] ++ pre l ++ pre r

data YesNo = Yes | No deriving (Eq)

-- toString :: YesNo a -> Str
-- toString a = if Yes == a then "yes" else "no"
-- toString a
-- \| Yes == a = "yes"
-- \| No == a = "no"
-- \| otherwise = "Error"

toString :: YesNo -> [Char]
toString No = "No"
toString Yes = "Yes"

-- kvartopirska
data Barva = Kriz | Pik | Srce | Karo
  deriving (Show, Enum)

-- deriving (Read, Show, Enum, Eq, Ord)

-- deriving (Read, Show, Enum, Eq, Ord)
newtype TwoToTen = TwoToTen Int

twoToTen :: Int -> Maybe TwoToTen
twoToTen x
  | x >= 2 && x <= 10 = Just (TwoToTen x)
  | otherwise = Nothing

data Stopnja = As | Kralj | Baba | Jack | Deset | Devet | Osem | Sedem | Sest | Pet | Stir | Tri | Dva
  deriving (Show, Enum, Eq)

-- deriving (Read, Show, Enum, Eq, Ord)

data Karta = Karta
  { vrednost :: Stopnja,
    barva :: Barva
  }
  deriving (Show)

instance Enum Karta where
  toEnum n = let (v, s) = n `divMod` 4 in Karta (toEnum v) (toEnum s)
  fromEnum c = fromEnum (vrednost c) * 4 + fromEnum (barva c)

type Karte = [Karta]

karte :: Karte
karte = [Karta v Pik | v <- [As .. Jack]]

barveKarte :: Karta -> Barva
barveKarte = barva

vrednostKarte :: Karta -> Stopnja -> Int
vrednostKarte vrednost x
  | x `elem` [Kralj, Baba, As, Jack] = 10 + fromEnum x
  | otherwise = fromEnum x + 2

-- kupcek :: [(Stopnja, Barva)]
kupcek = [(Karta As Pik), (Karta As Srce)]

caz x y = Karta x y

sumKupcka :: Stopnja -> Int
sumKupcka As = 1
sumKupcka Kralj = 13
sumKupcka Baba = 12
sumKupcka Jack = 11

-- let testKarta = Karta As Pik

-- veljavnaKarta :: Karta -> Bool
-- veljavnaKarta x
-- \|
-- let samoBarva = barveKarta testKarta

-- toString otherwise "Error"

-- solve :: [Int] -> [Int] -> Int
-- readIntList :: IO [Int]
-- readIntList =
--   do line <- getLine
--     return
--     $ map read
--     $ words line
--
-- main = do [n, m] <- readIntList
