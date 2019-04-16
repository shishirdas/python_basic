

dictionaryExample = {
					"name" :"shishir",

					"id"  :"1234560",
					"year" :"3rd"
					}


# dictionaryExample["name"] = "joy"

# print(dictionaryExample.get("name"))

for x, y in dictionaryExample.items():
	print(x)
	print("-")
	print(y)

del dictionaryExample["name"]

print(dictionaryExample)


