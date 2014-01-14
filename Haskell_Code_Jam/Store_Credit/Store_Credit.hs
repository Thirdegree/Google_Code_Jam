find_items (x:xs) total = 
	let item = filter (\t -> t+x==total) xs
	in if item /= [] then (x, item)
					else find_items xs total





main = do
	t<-getLine
	putStr t