import importlib

def get_closest_object(self,objects,pw):
	closer = objects[0]
	for object in objects:
		if pw.distance(object,self) < pw.distance(closer,self):
			closer = object
	return closer
	
	
def get_weakest_planet(planets):
	weakest = planets[0]
	for planet in planets:
		if planet.num_ships() < weakest.num_ships():
			weakest = planet
	return weakest
	
	
def is_valid_attack(attack,planet):
	if attack.num_ships() > planet.num_ships():
		return False
	else:
		return True
		

def get_lucrative_planets(planets,fleet):
	lucrative_planets = []
	for planet in planets:
		total_num_ships = planet.num_ships() + fleet.turns_remaining()*planet.growth_rate()  
		if total_num_ships <= fleet.num_ships():
			lucrative_planets.append(planet)
	return lucrative_planets
	
	
def final_attack(planets):
	if len(planets) == 1:
		return True
	else:
		return False
		

def do_turn(pw):

	if len(pw.my_fleets()) >= 1:
		return

	if len(pw.my_planets()) == 0:
		return
	for planet in pw.my_planets():
		source = planet
		dest = get_closest_object(source,pw.enemy_planets() + pw.neutral_planets(),pw)
		num_ships = source.num_ships() * 0.7
		pw.issue_order(source, dest, num_ships)
	
	
