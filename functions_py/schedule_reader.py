from functions_py.Flight_gl import Flight

def read_flights_from_file(filename, cost_class, aircraft, aircraft_rule):
    flights = []
    with open(filename, 'r') as file:
        tem_id = 1
        for line in file:
            data = [item for item in line.strip().split(',')]
            if len(data) >= 1:
                departure_city, arrival_city, departure_time, arrival_time, flight_number, aircraft_type = data
                flight_id = f"FL{tem_id}"
                if int(aircraft_type) not in aircraft_rule:
                    print('Aircraft type not allowed')
                    print(aircraft_type)
                    print(aircraft_rule)
                    continue
                try:
                    cost = int(cost_class.get_flight_cost())  # Convert cost to integer
                    flight = Flight(departure_city, arrival_city, cost, flight_id, departure_time, arrival_time)
                    flights.append(flight)
                    tem_id += 1
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
            else:
                print(f"Skipping invalid line: {line.strip()}")
    return flights