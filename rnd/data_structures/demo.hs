{-# LANGUAGE OverloadedStrings #-}
{-# OPTIONS_GHC -fno-warn-unused-imports #-}

module Demo where

-- import Distribution.Simple (KnownExtension (OverloadedStrings))
-- import Main (Project (ProjectGroupe))
import Project
import Reporting

someProject :: Project
someProject = ProjectGroupe "Sweden" [stockholem, gothenberg]
  where
    stockholem = Project 1 "StockHolm"
    gothenberg = Project 2 "Gothenburg"
    malmo = ProjectGroupe "Malmo" [city, limhamn]
    city = Project 3 "City"
    limhamn = Project 3 "Limhamn"
