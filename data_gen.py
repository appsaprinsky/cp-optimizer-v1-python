from datetime import datetime, timedelta

def parse_ssim_line(line):
    parts = line.split()
    flight_number = parts[1]
    departure_airport = parts[6]
    arrival_airport = parts[7]
    start_date = datetime.strptime(parts[3], "%Y%m%d")
    end_date = datetime.strptime(parts[4], "%Y%m%d")
    days_of_week = parts[5]
    departure_time = parts[8][:2] + ":" + parts[8][2:] + ":00"
    arrival_time = parts[9][:2] + ":" + parts[9][2:] + ":00"
    aircraft_type = parts[10]
    
    return (flight_number, departure_airport, arrival_airport, start_date, end_date, days_of_week, departure_time, arrival_time, aircraft_type)

def generate_schedule(line):
    flight_number, dep_airport, arr_airport, start_date, end_date, days_of_week, dep_time, arr_time, aircraft = parse_ssim_line(line)
    
    days_of_week = set(int(d) for d in days_of_week if d.isdigit())
    current_date = start_date
    output_lines = []
    
    while current_date <= end_date:
        if current_date.isoweekday() in days_of_week:
            formatted_date = current_date.strftime("%d-%m-%Y")
            output_lines.append(f"{dep_airport},{arr_airport},{formatted_date} {dep_time},{formatted_date} {arr_time},{flight_number},{aircraft}")
        current_date += timedelta(days=1)
    
    return output_lines

# Read SSIM file and process each line
ssim_file = "input_py/ssim_ai_gen.txt"  # Update this with the actual filename
output = []
with open(ssim_file, "r") as file:
    for line in file:
        if line.strip():
            output.extend(generate_schedule(line))

# Write output to file
with open("debug/ssim_schedule.txt", "w") as file:
    for line in output:
        file.write(line + "\n")

