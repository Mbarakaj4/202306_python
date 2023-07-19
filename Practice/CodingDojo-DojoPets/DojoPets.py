from Ninja import Ninja
import Pet

cat = Pet.Pets("catto", "cat", "generic food", "100%", "full")
blue_ninja = Ninja("blue","ninja","generic treats", "generic food", cat)

blue_ninja.feed()
blue_ninja.walk()
blue_ninja.shower()
blue_ninja.pet.noise()

gatete = Pet.Cat("Michiatto", "generic food", "100%", "full")
red_ninja = Ninja("red","ninja","generic treats", "generic food", gatete)

red_ninja.feed()
red_ninja.walk()
red_ninja.shower()
red_ninja.pet.noise()