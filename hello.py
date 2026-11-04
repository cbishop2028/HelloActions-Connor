import os
from datetime import datetime

def main():
    # 6. Use a default value if WHO_TO_GREET is unavailable
    who_to_greet = os.environ.get("WHO_TO_GREET", "Guest")
    
    # 7. Print a greeting
    print(f"Hello {who_to_greet}!")
    
    # 8. Print a second message explaining where it ran
    print("This program is running inside GitHub Actions.")
    
    # Optional Challenge: Display the current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Execution Timestamp: {current_time}")

if __name__ == "__main__":
    main()
