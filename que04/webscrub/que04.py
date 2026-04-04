import requests
from bs4 import BeautifulSoup
import csv
import os

# URL to scrape
URL = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"

# CSV file name
CSV_FILE = "books.csv"

# Convert word rating to number
def convert_rating(word):
    if word == "One":
        return 1
    elif word == "Two":
        return 2
    elif word == "Three":
        return 3
    elif word == "Four":
        return 4
    elif word == "Five":
        return 5
    else:
        return 0

# Scrape books from webpage
def scrape_books():
    print("Connecting to website...")
    print(f"URL: {URL}\n")

    # Send request to website
    response = requests.get(URL)

    # Check if request was successful
    if response.status_code != 200:
        print(f"Failed to connect. Status code: {response.status_code}")
        return []

    print("Connected successfully!")

    # Parse the webpage content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all book items on the page
    book_list = soup.find_all("article", class_="product_pod")

    print(f"Found {len(book_list)} books\n")

    # Store all books data
    books = []

    for book in book_list:

        # Get the book title from the anchor tag
        title = book.find("h3").find("a")["title"]


        rating_word = book.find("p", class_="star-rating")["class"][1]

        # Convert rating word to number
        rating = convert_rating(rating_word)

        # Get the price text
        price = book.find("p", class_="price_color").text.strip()

        # Add book to list
        books.append({
            "title":  title,
            "rating": rating,
            "price":  price
        })

        print(f"Title  : {title}")
        print(f"Rating : {rating} stars")
        print(f"Price  : {price}")
        print("-" * 50)

    return books


# Save books data to CSV file
def save_to_csv(books):
    print(f"\nSaving data to {CSV_FILE}...")

    # Open CSV file for writing
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        # Define column names
        fieldnames = ["title", "rating", "price"]

        # Create CSV writer
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header row
        writer.writeheader()

       
        for book in books:
            writer.writerow(book)

    print(f"Saved {len(books)} books to {CSV_FILE}")


# Read and display data from CSV file
def read_from_csv():
    print(f"\nReading data from {CSV_FILE}...")
    print("=" * 60)
    print(f"{'Title':<45} {'Rating':<8} {'Price'}")
    print("=" * 60)

    # Check if file exists
    if not os.path.exists(CSV_FILE):
        print("CSV file not found!")
        return

    # Open CSV file for reading
    with open(CSV_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

       
        total = 0

        for row in reader:
            title = row["title"][:44]
            rating = row["rating"] + " stars"
            price = row["price"]
            print(f"{title:<45} {rating:<8} {price}")
            total += 1

    print("=" * 60)
    print(f"Total books: {total}")
    print("=" * 60)


# Main function
def main():
    print("=" * 60)
    print("   Task04 - Books Web Scraper")
    print("=" * 60)

   
    books = scrape_books()

   
    if not books:
        print("No books found!")
        return

    save_to_csv(books)

   
    read_from_csv()

    print("\nDone!")


if __name__ == "__main__":
    main()