import sys

def my_function():
    pass

def main():
    """
    This script ...
    """
    # Open a text file containing an output of show version
    # Read the output
    # Turn the output into a list so that we can check each line
    file_name = "template_show-version.txt"
    with open(file_name) as file:
        data_list = file.readlines()

    # Search each line for the information you want
    # Save each peace of information to a variable
    for line in data_list:
        if "uptime" in line:
            tmp_list = line.split(" ")
            hostname = tmp_list[0]

        if "ROM:" in line:
            tmp_list = line.split(" ")
            version = tmp_list[1]

    # Display the information to the screen
    print(f"Device {hostname} is running version {version}")

# Standard call to the main() function
if __name__ == '__main__':
    # print(f"List of command line arguments passed to the script.\n{sys.argv}\nThe first element is: ")
    main()