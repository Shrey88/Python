from collections import namedtuple

PlantDetails = namedtuple('PlantDetails', ['scientific_name', 'lifecycle', 'plant_type'])

named_plants_dict = {
    "Andromeda": PlantDetails("Pieris japonica", "Evergreen", "Shrub"),
    "Bellflower": PlantDetails("Campanula", "Annual, biennial, perennial", "Flower"),
    "China Pink": PlantDetails("Dianthus", "Perennial", "Flower"),
    "Daffodil": PlantDetails("Narcissus", "Perennial", "Flower"),
    "Evening Primrose": PlantDetails("Oenothera", "Biennial", "Flower"),
    "French Marigold": PlantDetails("Tagetes patula", "Annual", "Flower"),
    "Golden Hakone Grass": PlantDetails("Hakonechloa macra", "Perennial", "Grass"),
    "Hydrangea": PlantDetails("Hydrangea", "Deciduous, evergreen", "Shrub"),
    "Iris": PlantDetails("Iris", "Perennial", "Flower"),
    "Japanese Camellia": PlantDetails("Camellia japonica", "Evergreen", "Shrub"),
    "Lavender": PlantDetails("Lavendula", "Perennial", "Shrub"),
    "Lilac": PlantDetails("Syringa vulgaris", "Deciduous", "Shrub"),
    "Magnolia": PlantDetails("Magnolia", "Deciduous, evergreen", "Shrub"),
    "Peony": PlantDetails("Paeonia", "Perennial", "Shrub"),
    "Queen Anne's Lace": PlantDetails("Daucus carota", "Biennial", "Flower"),
    "Red Hot Poker": PlantDetails("Kniphofia", "Perennial", "Flower"),
    "Snapdragon": PlantDetails("Antirrhinum majus", "Annual", "Flower"),
    "Sunflower": PlantDetails("Helianthus", "Annual", "Flower"),
    "Tiger Lily": PlantDetails("Lilinium tigrinium", "Perennial", "Flower"),
    "Witch Hazel": PlantDetails("Hamamelis", "Deciduous", "Shrub"),
}


if any([type.plant_type == "Grass" for type in named_plants_dict.values()]):
    print("Contains grass in this pack.")
else:
    print("No grasses in this pack")


if any([type.plant_type == "Cactus" for type in named_plants_dict.values()]):
    print("Contains Cactus in this pack.")
else:
    print("No Cactus in this pack")