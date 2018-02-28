from itertools import combinations

def count_required_resources(required_resources):
	resources = []
	resource_count = []
	for resource in required_resources:
		if resource in resources:
			resource_count[resources.index(resource)] += 1
		else:
			resources.append(resource)
			resource_count.append(1)
	resource_triple = [list(r) for r in zip(resources, resource_count)]
	for r in resource_triple: r.append([])
	# each resource list = [resource, remaining count, card indices] 
	return resource_triple

def first_pass(cards, resource_triple):
	# Eliminate single resource cards
	for resource in resource_triple:
		if resource[0] in cards:
			resource[2] = [cards.index(resource[0])]
			resource[1] -= len(resource[2])
			cards[cards.index(resource[0])] = -1
	# TODO: Arrange from largest to smallest count

def iterate(cards, resource_triple):
	indices = []
	# Find all possible resource card indices
	for index, card in enumerate(cards):
		if card != -1:
			if resource_triple[0][0] in card:
				indices.append(index)
	# Check on available resource cards
	if len(indices) >=  resource_triple[0][1]:
		# Recursively iterate through all combinations
		for combo in combinations(indices, resource_triple[0][1]):
			cards_less = list(cards)
			for x in combo: cards_less[x] = -1
			resource_triple_less = list(resource_triple)
			resource = list(resource_triple_less[0])
			del resource_triple_less[0]
			resource[2] = resource[2] + list(combo)
			if len(resource_triple_less) > 0:
				bool_iterate, resource_triple_return = iterate(cards_less, resource_triple_less)
				if bool_iterate:
					resource_triple_return.append(resource)
					return True, resource_triple_return
				else:
					return False, resource_triple
			# We've successfully assigned all resource cards
			else:
				resource_triple = [resource]
				return True, resource_triple
	# Required resource cards don't exist
	else:
		return False, resource_triple

cards = ['W/B/S/O', 'W', 'S/B', 'S']
required_resources = 'WWSS'
#cards = ['W/B/S/O', 'S/O', 'W/S', 'W/B', 'W/B', 'W', 'B']
#required_resources = 'WWBSSOO'
resource_triple = count_required_resources(required_resources)
first_pass(cards, resource_triple)
bool_iterate, resource_triple_final = iterate(cards, resource_triple)
if resource_triple is resource_triple_final:
	print("Impossible!")
else:
	print("Combination: ", resource_triple_final)
