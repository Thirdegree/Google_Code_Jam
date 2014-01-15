--This makes so much more sense for haskell. 
--once again, formating input was more a pain than actually doing what was needed.

import Data.List

parse t = [words x | x<-lines t]

reverse' = foldr1 (++) . intersperse " " . reverse

happens_here n (x:xs) = 
	("Case #" ++ show n ++ ": " ++ x) : happens_here (n+1) xs
happens_here _ [] = [""]

main = do
	inp <- readFile "input_large.txt"
	let parsed = tail (parse inp)
	writeFile "output_large.txt" $ unlines $ happens_here 1 $ map reverse' parsed
