import libertybooks

def main():
    # test isbn of moby dick
    name = input("Enter name: ")
    priceLibertyBooks = libertybooks.getPricesAndNames(name)
    print(priceLibertyBooks)

if __name__ == "__main__":
    main()