import tkinter as tk
from tkinter import messagebox
import requests

def get_city():
    try:
        # Fetch IP address from a service
        response = requests.get("https://api64.ipify.org?format=json")
        ip_data = response.json()
        ip_address = ip_data["ip"]

        # Use IPinfo API to get geolocation data
        access_token = "YOUR_IPINFO_ACCESS_TOKEN"  # Replace with your actual IPinfo access token
        response = requests.get(f"https://ipinfo.io/{ip_address}?token={access_token}")
        location_data = response.json()

        # Get the city from the location data
        city = location_data.get("city", "Unknown")

        # Display the city in a message box
        messagebox.showinfo("City Information", f"Your city is: {city}")
    except Exception as e:
        # Show an error message if there was an issue getting the city
        messagebox.showerror("Error", f"Error occurred: {e}")

def main():
    root = tk.Tk()
    root.title("City Finder")

    # Create a label
    label = tk.Label(root, text="Click the button to find your city:")
    label.pack(pady=10)

    # Create a button to trigger the city retrieval
    button = tk.Button(root, text="Get City", command=get_city)
    button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
