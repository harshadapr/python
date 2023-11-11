def km_to_miles(km):
    miles = km / 1.60934
    return miles

kilometers = 10
miles = km_to_miles(kilometers)
print(f"{kilometers} kilometers is equal to {miles:.2f} miles")
