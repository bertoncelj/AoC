-- module Databese where
--
-- import Project
-- import System.Random (getStdRandom, randomR)
--
-- getBudget :: ProjectId -> IO Budget
-- getBudget _ = do
--   income <- Money <$> getStdRandom (randomR (0, 10000))
--   expenditure <- Money <$> getStdRandom (randomR (0, 10000))
--   pure Budget {budgetIncome = income, budgetExpenditure = expenditure}
--
-- getTransactions :: ProjectId -> IO [Transaction]
-- getTransactions _ = do
--   sale <- Sale . Money <$> getStdRandom (randomR (0, 4000))
--   purchase <- Purchase . Money <$> getStdRandom (randomR (0, 4000))
--   pure [sale, purchase]
--

module Database where

import Project
import System.Random (getStdRandom, randomR)

getBudget :: ProjectId -> IO Budget
getBudget _ = do
  income <- Money <$> getStdRandom (randomR (0, 10000))
  expenditure <- Money <$> getStdRandom (randomR (0, 10000))
  pure Budget {budgetIncome = income, budgetExpenditure = expenditure}

getTransactions :: ProjectId -> IO [Transaction]
getTransactions _ = do
  sale <- Sale . Money <$> getStdRandom (randomR (0, 4000))
  purchase <- Purchase . Money <$> getStdRandom (randomR (0, 4000))
  pure [sale, purchase]
