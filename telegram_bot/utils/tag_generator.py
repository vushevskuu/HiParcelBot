def generate_tags(departure_city, destination_city, departure_date, parcel_description):
    tags = []
    tags.append(f"#{departure_city.replace(' ', '')}")
    tags.append(f"#{destination_city.replace(' ', '')}")
    tags.append(f"#{departure_date.replace('.', '')}")

    if "документы" in parcel_description.lower():
        tags.append("#documents")
    elif "одежда" in parcel_description.lower():
        tags.append("#clothes")
    elif "электроника" in parcel_description.lower():
        tags.append("#electronics")

    tags.append(f"#{departure_city.replace(' ', '')}{destination_city.replace(' ', '')}")

    return tags

# Пример использования
tags = generate_tags("Москва", "Санкт-Петербург", "15.03.2024", "Документы, формат А4, вес 1 кг")
print(tags)