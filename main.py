import libertybooks

def main():
    isbn = 9780747532743
    priceLibertyBooks = libertybooks.get_price_by_isbn(isbn)

if __name__ == "__main__":
    main()