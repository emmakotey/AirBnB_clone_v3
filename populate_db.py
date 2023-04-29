 #!/usr/bin/python3
  2 
  3 from models.city import City
  4 from models.state import State
  5 from models import storage
  6 
  7 state = State(name="California")
  8 storage.new(state)
  9 
 10 cities = [
 11     City(name="Los Angeles", state_id=state.id),
 12     City(name="San Francisco", state_id=state.id),
 13     City(name="San Diego", state_id=state.id)
 14 ]
 15 
 16 for city in cities:
 17     storage.new(city)
 18     storage.save()
