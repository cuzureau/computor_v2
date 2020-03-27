basic_tests = [
	# NUM + NUM
	#	  | NUMi
	#	  | (NUMi)
	#	  | (NUMi @ NUM)
	"A @ B",
	"A @ Bi",
	"A @ (Bi)",
	"A @ (Bi @ A)",
	# NUMi 			+ NUM
	# (NUMi) 		| NUM
	# (NUMi @ NUM) 	| NUM
	"Ai @ B",
	"(Ai) @ B",
	"(Ai @ B) @ B",

##########################################
	# NUMi + NUMi
	#  	   | (NUMi)
	#      | (NUMi @ NUM)
	"Ai @ Bi",
	"Ai @ (Bi)",
	"Ai @ (Bi @ A)",
	# (NUMi) 		+ NUMi
	# (NUMi @ NUM)	| NUMi
	"(Ai) @ Bi",
	"(Ai @ B) @ Bi",

##########################################
	# (NUMi) + (NUMi)
	# (NUMi) | (NUMi @ NUM)
	"(Ai) @ (Bi)",
	"(Ai) @ (Bi @ A)",
	# (NUMi @ NUM)	+ (4Bi)
	"(Ai @ B) @ (Ai)",

##########################################
	# (NUMi @ NUM) + (NUMi @ NUM)
	"(Ai @ B) @ (Bi @ A)",
]