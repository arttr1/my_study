# описание автомобиля через функции

def create_car(color, consumption, tank_volume, mileage = 0):

    return {
        "color": color,
        "consuption": consumption,
        "tank_volume": tank_volume,
        "reserve": tank_volume, 
        "mileage":mileage,
        "engine_on":False

    }

def start_engine(car):
    if not car["engine_on"] and car["reserve"] > 0:
        car["engine_on"] = True
        return "engine is on now"
    return "engine is already on"


# car = create_car('red', 10, 55)