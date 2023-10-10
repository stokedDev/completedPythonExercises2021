numbers = [1, 2, 3, 4, 5, 6]
foods = ["pizza", "curry", "sushi", "poke", "salad"]
# foods.extend(numbers) .extend() appends a list to another list
print(foods)
foods.append("eggs")
# foods.extend(numbers)
print(foods)
foods.insert(4, "sausage")
# the above code inserts "sausage" at index 4
foods.remove("salad")
# foods.clear() will remove all list elements
print(foods)
# .pop() removes last item from list
print(foods.index("sushi"))
# .index() can tell what index something is
foods.insert(4, "pizza")
print(foods.count("pizza"))
foods.sort()  # puts in alphabetical order or ascending order for numbers
print(foods)
numbers.reverse()  # reverses order
print(numbers)
foods2 = foods.copy()
foods2.reverse()
print(foods2)
