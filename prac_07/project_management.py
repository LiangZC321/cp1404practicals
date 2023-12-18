import datetime
from project import Project

def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            data = line.strip().split('\t')
            projects.append(Project(*data))
    return projects

def save_projects(filename, projects):
    with open(filename, 'w', newline='') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")

def display_projects(projects):
    print("Incomplete projects:")
    for project in projects:
        if not project.is_complete():
            print(f"  {project}")
    print("Completed projects:")
    for project in projects:
        if project.is_complete():
            print(f"  {project}")

def filter_projects_by_date(projects, date):
    filtered_projects = [project for project in projects if project.start_date > date]
    for project in filtered_projects:
        print(f"  {project}")

def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    percent_complete = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))

def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    selected_project = projects[choice]
    new_percentage = input(f"New Percentage: ")
    new_percentage = new_percentage or selected_project.completion_percentage

    new_priority = input(f"New Priority: ")
    new_priority = new_priority or selected_project.priority
    selected_project.update(int(new_percentage), int(new_priority))

def main():
    filename = "projects.txt"
    projects = load_projects(filename)

    while True:
        print("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
              "- (A)dd new project\n- (U)pdate project\n- (Q)uit")
        choice = input(">>> ").lower()
        if choice == 'q':
            print("Thank you for using custom-built project management software.")
            break
        elif choice == 'l':
            projects = load_projects(filename)
        elif choice == 's':
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            filter_projects_by_date(projects, date)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)
main()
