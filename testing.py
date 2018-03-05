from classes import *


print("Testing function get_valid_input():")
print(get_valid_input("what laundry?", ("coin", "ensuite", "none")))

print()
print("For HouseRental class, in example, all the parent classes of it must\n"
      "be functioning. So, I will be testing only children classes.\n")

print("Testing HouseRental class:")
init = HouseRental.prompt_init()
house = HouseRental(**init)
house.display()

print("Testing ApartmentRental class:")
init = ApartmentRental.prompt_init()
apartment = ApartmentRental(**init)
apartment.display()

print("Testing HousePurchase class:")
init = HousePurchase.prompt_init()
house = HousePurchase(**init)
house.display()

print("Testing ApartmentPurchase class:")
init = ApartmentPurchase.prompt_init()
apartment = ApartmentPurchase(**init)
apartment.display()

print("Testing Agent class:")
agent = Agent()
print("Adding first property:")
agent.add_property()
print("Adding second property:")
agent.add_property()
print("Displaying properties:")
agent.display_properties()

print("Testing my methods:")
print("Printing all properties with type 'house':")
agent.display_chosen_properties("house")
print("Printing all properties with types 'apartment' and 'rental':")
agent.display_chosen_properties("apartment", "rental")
print("Removing all properties of the agent and displaying them to show they are gone:")
agent.clear_property()
agent.display_properties()

print("\nFinished testing. Testing was successful!")
