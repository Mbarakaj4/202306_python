from Ninja import Ninja
from Pet import Pets

cat = Pets("catto", "cat", "generic food", "100%", "full")
blue_ninja = Ninja("blue","ninja","generic food", cat)

blue_ninja.feed()
blue_ninja.walk()
blue_ninja.shower()