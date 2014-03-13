main = do
	l <- readFile "test_doc"
	let lined_l = lines l
	let lined_reversed_l = map reverse lined_l
	let joined = unlines lined_reversed_l
	writeFile "output" joined