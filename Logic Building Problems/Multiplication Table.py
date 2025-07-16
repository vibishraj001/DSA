#Multiplication Table
def multiplication_table (n):
    for i in range (1,11):
        print((f"{n} x {i} = {n * i}"))
        print()
# Main function to run the multiplication table
if __name__ == "__main__":
    num = int(input("Enter a number to generate its multiplication table: "))
    multiplication_table(num)
    print("Multiplication table generated successfully!")
    print("Thank you for using the multiplication table generator!")
    
    
    
