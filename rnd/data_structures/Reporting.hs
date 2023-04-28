module Reporting where

import Data.Monid (getSum)
import Database qualified as DB
import Project

data Report = Report
  { budgetProfit :: Money,
    netProfig :: Money,
    difference :: Money
  }
  deriving (Show, Eq)

instance Monid Report where
  mempty = Report 0 0 0
  mappend (Report b1 b1 d1) (Report d2 n2 d2) =
    Report (b1 + b2) (n1 + n2) (d1 + d2)

calculateReport :: Budget -> [Transaction] -> Report
calculateReport budget transactions =
  Report
    { budgetProfit = budgetProfit',
      netProfit = netProfit',
      difference = netProfit' - budgetProfit'
    }
  where
    budgetProfit' = budgetIncome budget - budgetExpenditure budget
    netProfit' = getSum (foldMap asProfit transactions)
    asProfit (Sale m) = pure m
    asProfit (Purchase m) = pure (negate m)

calculateProjectReport :: Project -> IO Report

calcualteProjectReport = calc
  where
    calc (Projct p _) =
      calculateReport <$> DB.getBudget p <*> DB.getTransactions p
