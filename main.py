# Function to calculate average grade
def calculate_average(grades):
    return sum(grades) / len(grades)

# Function to determine status
def get_status(average):
    if average >= 75:
        return "Passed"
    else:
        return "Failed"

# Main execution
def main():
    print("--- Student Grade Calculator ---")
    
    # List to store scores
    scores = [85, 90, 78, 92, 88]
    
    # Calculate statistics
    avg = calculate_average(scores)
    status = get_status(avg)
    
    # Display results
    print(f"Scores: {scores}")
    print(f"Average Grade: {avg:.2f}")
    print(f"Final Status: {status}")

if __name__ == "__main__":
    main()