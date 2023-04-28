{-# LANGUAGE GeneralizedNewtypeDeriving #-}

module Project where

import Data.Text (Text)

newtype Money = Money
  { unMoney :: Double
  }
  deriving (Show, Eq, Num)

newtype ProjectId = ProjectId
  { unProjectId :: Int
  }
  deriving (Show, Eq, Num)

data Project
  = Project ProjectId Text
  | ProjectGroupe Text [Project]
  deriving (Show, Eq)

data Buget = Buget
  { bugetIncome :: Money,
    bugetExpanditure :: Money
  }
  deriving (Show, Eq)

data Transaction
  = Sale Money
  | Purchase Money
  deriving (Show, Eq)
