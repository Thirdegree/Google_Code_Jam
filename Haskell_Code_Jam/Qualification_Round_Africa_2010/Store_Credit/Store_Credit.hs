import Data.List

check_all :: Int -> [Int] -> Maybe Int
check_all total (x:y:ys) = 
	if x+y == total then Just y else check_all total (x:ys)
check_all total (x:[]) = Nothing

find_items :: Int -> [Int] -> [Int]
find_items total (x:xs) = 
	case check_all total (x:xs) of
						Just n -> [x, n]
						Nothing -> find_items total xs
find_items total [] = []

find_indexs :: [Int] -> [Int] -> [Int]
find_indexs xs ys = case map (\t -> elemIndices t ys) xs of 
						[[x],[y]] -> [x+1,y+1]
						[[x,y],[_,_]] -> [x+1,y+1]
						_ -> error "Oops!"

toInt :: [String] -> [Int]
toInt xs = map (\t -> read t :: Int) xs

toString :: [Int] -> [String]
toString xs = map (\t -> show t) xs

parser t = [words x | x <- lines t] 

everything_happens_here (x:total:_:list:xs) = 
	(find_indexs items list):everything_happens_here ([n-1]:xs)
	where
		items = find_items (head total) list
		n = head x
everything_happens_here ts = []

toOut n (x:xs) = "Case #" ++ show n ++ ": " ++ (foldl1 (++) sol) ++ "\n" ++ toOut (n+1) xs
	where 
		sol = intersperse " " (toString x)
toOut _ _ = ""


main = do
	inp <- readFile "input_large.txt"
	let parsed = map toInt (parser inp)
	let answers = everything_happens_here parsed
	let output = toOut 1 answers
	writeFile "output_large.txt" output
