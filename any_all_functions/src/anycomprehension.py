from collections import namedtuple

Plant = namedtuple('Plant', ['name', 'scientific_name', 'lifecycle', 'plant_type'])

named_plants_list = [
    Plant("Andromeda", "Pieris japonica", "Evergreen", "Shrub"),
    Plant("Bellflower", "Campanula", "perennial", "Flower"),
    Plant("China Pink", "Dianthus", "Perennial", "Flower"),
    Plant("Daffodil", "Narcissus", "Perennial", "Flower"),
    Plant("Evening Primrose", "Oenothera", "Biennial", "Flower"),
    Plant("French Marigold", "Tagetes patula", "Annual", "Flower"),
    Plant("Golden Hakone Grass", "Hakonechloa macra", "Perennial", "Grass"),
    Plant("Hydrangea", "Hydrangea", "evergreen", "Shrub"),
    Plant("Iris", "Iris", "Perennial", "Flower"),
    Plant("Japanese Camellia", "Camellia japonica", "Evergreen", "Shrub"),
    Plant("Lavender", "Lavendula", "Perennial", "Shrub"),
    Plant("Lilac", "Syringa vulgaris", "Deciduous", "Shrub"),
    Plant("Magnolia", "Magnolia", "Deciduous, evergreen", "Shrub"),
    Plant("Peony", "Paeonia", "Perennial", "Shrub"),
    Plant("Queen Anne's Lace", "Daucus carota", "Biennial", "Flower"),
    Plant("Red Hot Poker", "Kniphofia", "Perennial", "Flower"),
    Plant("Snapdragon", "Antirrhinum majus", "Annual", "Flower"),
    Plant("Sunflower", "Helianthus", "Annual", "Flower"),
    Plant("Tiger Lily", "Lilinium tigrinium", "Perennial", "Flower"),
    Plant("Witch Hazel", "Hamamelis", "Deciduous", "Shrub"),
]

if any([plant.plant_type == "Grass" for plant in named_plants_list]):
    print("This pack contains grass")
else:
    print("No grasses in this pack")