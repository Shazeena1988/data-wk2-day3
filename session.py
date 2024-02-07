dinosaurs = [
    "Triceratops",
    "Velociraptor",
    "Anklyosaurus",
    "Archaeopteryx",
    "Tyrannosaurus Rex",
    "Stegosaurus",
    "Iguanodon"
]

saurus_dinosaurs = []

for dino in dinosaurs:
    if "saurus" in dino:
        saurus_dinosaurs.append(dino)

print(saurus_dinosaurs)