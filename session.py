dinosaurs = [
    "Triceratops",
    "Velociraptor",
    "Anklyosaurus",
    "Archaeopteryx",
    "Tyrannosaurus Rex",
    "Stegosaurus",
    "Iguanodon"
]

saurus_dinosaurs = [
    "Anklyosaurus",
    "Tyrannosaurus Rex",
    "Stegosaurus"
]

for dino in dinosaurs:
    if "saurus" in dino:
        saurus_dinosaurs.append(dino)

print(saurus_dinosaurs)