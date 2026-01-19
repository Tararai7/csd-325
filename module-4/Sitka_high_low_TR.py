# sitka_high_low_TR.py
# Tara Rai 
# Assignment- M4.2 
# Date- 01/16/2026

import sys
import csv
from datetime import datetime
import matplotlib.pyplot as plt

def load_weather_data(filename):
    """Load dates, high, and low temperatures from CSV."""
    dates, highs, lows = [], [], []
    try:
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            # Locate columns by name (robust to column order)
            date_idx = header_row.index('DATE')
            high_idx = header_row.index('TMAX')
            low_idx = header_row.index('TMIN')

            for row in reader:
                current_date = datetime.strptime(row[date_idx], '%Y-%m-%d')
                try:
                    high = int(row[high_idx])
                    low = int(row[low_idx])
                except ValueError:
                    continue  # Skip rows with missing temp data
                else:
                    dates.append(current_date)
                    highs.append(high)
                    lows.append(low)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    return dates, highs, lows

def display_menu():
    """Display interactive menu to user."""
    print("\n--- Sitka Weather Data Viewer ---")
    print("1. View High Temperatures")
    print("2. View Low Temperatures")
    print("3. Exit")
    return input("Select an option (1-3): ").strip()

def plot_temperatures(dates, temps, title, color):
    """Generate and display temperature plot."""
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)
    ax.set_title(title, fontsize=20)
    ax.set_xlabel('', fontsize=14)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (°F)", fontsize=14)
    ax.tick_params(axis='both', labelsize=12)
    plt.show()

def main():
    filename = 'sitka_weather_2021_simple.csv'
    dates, highs, lows = load_weather_data(filename)

    while True:
        choice = display_menu()
        if choice == '1':
            plot_temperatures(dates, highs, "Daily High Temperatures - 2021", 'red')
        elif choice == '2':
            plot_temperatures(dates, lows, "Daily Low Temperatures - 2021", 'blue')
        elif choice == '3':
            print("Thank you for using the Sitka Weather Viewer. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()