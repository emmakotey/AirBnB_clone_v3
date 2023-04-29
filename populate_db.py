#!/usr/bin/python3
from models.city import City
from models.state import State
from models import storage

state = State(name="California")
storage.new(state)

cities = [
    City(name="Los Angeles", state_id=state.id),
    City(name="San Francisco", state_id=state.id),
    City(name="San Diego", state_id=state.id)
]

for city in cities:
    storage.new(city)
    storage.save()

