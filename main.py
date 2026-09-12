def main():
    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == 1:
            Analyze_Logs()

        elif choice == 2:
            Show_SecuritySummary()

        elif choice == 3:
            Show_DetectedThreats()

        elif choice == 4:
            Search_IP()

        elif choice == 5:
            Generate_Report()

        elif choice == 6:
            print("The task is complete")
            break

        else:
            print("Invalid choice! Please try again.")


def show_menu():
    print("1. Analyze Logs")
    print("2. Show Security Summary")
    print("3. Show Detected Threats")
    print("4. Search IP")
    print("5. Generate Report")
    print("6. Exit")


def get_menu_choice():
    choice = int(input("Choice from the menu: "))
    return choice


logs = [
    {
        "timestamp": "09:15",
        "ip": "192.168.1.10",
        "username": "admin",
        "event": "login",
        "status": "success",
    },
    {
        "timestamp": "09:16",
        "ip": "192.168.1.15",
        "username": "john",
        "event": "login",
        "status": "failed",
    },
    {
        "timestamp": "09:16",
        "ip": "192.168.1.15",
        "username": "john",
        "event": "login",
        "status": "failed",
    },
    {
        "timestamp": "09:17",
        "ip": "192.168.1.15",
        "username": "john",
        "event": "login",
        "status": "failed",
    },
]


def Analyze_Logs():
    print("\n========== Analyze_Logs() ==========")

    a = input("Login your IP: ")

    count = 0
    failed_count = 0
    successful_count = 0

    found = False

    for i in logs:

        if a == i["ip"]:

            found = True
            count += 1

            if i["status"] == "failed":
                failed_count += 1
                print("⚠ Login attempt failed")

            else:
                successful_count += 1
                print("✓ Login successful")

    print("Total login attempts:", count)
    print("Total login failed attempts:", failed_count)
    print("Total login successful attempts:", successful_count)

    if failed_count >= 3:
        print("⚠ Suspicious activity detected")

    if found == False:
        print("IP wasn't found in the logs")


def Show_SecuritySummary():
    print("\n========== Show_SecuritySummary() ==========")

    Total_Events = 0
    successful_count = 0
    failed_count = 0

    ip_addresses = set()
    failed_by_ip = {}

    for log in logs:

        ip_addresses.add(log["ip"])
        Total_Events += 1

        if log["status"] == "success":
            successful_count += 1

        elif log["status"] == "failed":

            failed_count += 1

            ip = log["ip"]

            if ip in failed_by_ip:
                failed_by_ip[ip] += 1

            else:
                failed_by_ip[ip] = 1

    print("Total login attempts:", Total_Events)
    print("Successful Logins:", successful_count)
    print("Failed Logins:", failed_count)
    print("Unique IP Addresses:", len(ip_addresses))
    print("Failed Logins by IP:", failed_by_ip)


def Show_DetectedThreats():
    print("\n========== Show_DetectedThreats() ==========")

    s = {}

    for i in logs:

        if i["status"] == "failed":

            if i["ip"] in s:
                s[i["ip"]] += 1

            else:
                s[i["ip"]] = 1

    for ip, count in s.items():

        if count >= 3:
            print("Threat: Possible Brute Force Attack")
            print("IP:", ip)
            print("Failed Attempts:", count)


def Search_IP():
    print("\n========== Search_IP() ==========")

    ip = input("Enter your IP for the search: ")

    found = False

    for i in logs:

        if i["ip"] == ip:

            print("The IP is already stored in the logs")
            found = True

    if found == False:
        print("The IP has not been found")


def Generate_Report():

    print("\n========== Generate_Report() ==========")

    count_attempts = 0
    successful_counter = 0
    failed_counter = 0

    ip_addresses = set()

    for i in logs:

        ip_addresses.add(i["ip"])
        count_attempts += 1

        if i["status"] == "success":
            successful_counter += 1

        elif i["status"] == "failed":
            failed_counter += 1

    print("\n========== SECURITY REPORT ==========")
    print("Total Login Attempts:", count_attempts)
    print("Successful Logins:", successful_counter)
    print("Failed Logins:", failed_counter)
    print("Unique IP Addresses:", len(ip_addresses))


# Run the terminal program only when main.py is executed directly
if __name__ == "__main__":
    main()