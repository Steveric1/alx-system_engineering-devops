import csv
import json
import sys
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    try:
        # Fetch user data
        u_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        with urllib.request.urlopen(u_url) as response:
            user_data = json.loads(response.read().decode())
            username = user_data.get('username')

        # Fetch tasks data
        t_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        with urllib.request.urlopen(t_url) as response:
            tasks_data = json.loads(response.read().decode())

        # Write data to CSV
        csv_file = f'{user_id}.csv'
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                      'TASK_TITLE']
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            # Write tasks to CSV
            for task in tasks_data:
                writer.writerow({
                    'USER_ID': user_id,
                    'USERNAME': username,
                    'TASK_COMPLETED_STATUS': 'Completed'
                    if task.get('completed') else 'Incomplete',
                    'TASK_TITLE': task.get('title')
                })

        print(f'Data has been exported to {csv_file}')
    except Exception as e:
        print("An error occurred:", e)
