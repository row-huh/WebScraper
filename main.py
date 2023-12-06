import libertybooks
import csv

def main():
    # test isbn of moby dick
    name = input("Enter name: ")
    # priceLibertyBooks = libertybooks.getPricesAndNames(name)
    book_details = libertybooks.getPricesAndNames(name)
    write_books_to_csv(book_details, "bookinfo.csv")




def write_books_to_csv(book_list, csv_filename):
    # Define the CSV header
    header = ['BOOK_NAME', 'AUTHOR_NAME', 'PRICE']

    # Create or overwrite the CSV file
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        # Create a CSV writer
        csv_writer = csv.writer(csv_file)

        # Write the header to the CSV file
        csv_writer.writerow(header)

        # Process each book information and write to the CSV file
        for book_info in book_list:
            # Split the book information into lines
            lines = book_info.split('\n')

            # Extract relevant information
            book_name = lines[0].strip()
            author_name = lines[1].replace('By: ', '').strip()
            price = lines[2].replace('Rs ', '').replace(',', '').strip()

            # Write the information to the CSV file
            csv_writer.writerow([book_name, author_name, price])
            
            
            
if __name__ == "__main__":
    main()