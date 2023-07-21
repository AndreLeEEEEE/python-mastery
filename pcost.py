def portfolio_cost(filename:str):
    with open(filename, 'r') as file:
        sum = 0
        for line in file:
            lis = line.split()
            try:
                qty = int(lis[1])
                price = float(lis[2])
            except ValueError as e:
                print(f"Couldn't parse {line}")
                print(f"Reason {e}")

            sum += qty * price

        return sum
    
if __name__ == "__main__":
    print(portfolio_cost('Data/portfolio.dat'))