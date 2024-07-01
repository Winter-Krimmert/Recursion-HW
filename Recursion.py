#!/usr/bin/env python3
# Task 1.
# 'list_tasks' will take a list of tasks (which can be nested) and print them in a structured format. Each task is a dictionary with a "name" and possibly a "subtasks" key, where "subtasks" is a list of futher tasks.

# Task 2.
def list_tasks(task_hierarchy, indent=0):
    for task in task_hierarchy:
        # Print the task name with appropriate indentation
        print(" " * indent + task["name"])
        # If the task has subtasks, recursively list them with increased indentation
        if "subtasks" in task:
            list_tasks(task["subtasks"], indent + 2)

# Task 3.

# Testing the function with task_hierarchy_1 and task_hierarchy_2.
# Sample task hierarchies for testing

task_hierarchy_1 = [
    {
        "name": "Project",
        "subtasks": [
            {"name": "Define project scope"},
            {"name": "Create project plan"},
            {
                "name": "Assign project team",
                "subtasks": [
                    {"name": "Identify team members"},
                    {"name": "Allocate roles and responsibilities"}
                ]
            },
            {"name": "Conduct project kickoff meeting"}
        ]
    },
    {
        "name": "Research",
        "subtasks": [
            {"name": "Gather data"},
            {
                "name": "Analyze data",
                "subtasks": [
                    {"name": "Data cleaning"},
                    {"name": "Statistical analysis"}
                ]
            },
            {"name": "Draw conclusions"}
        ]
    }
]

task_hierarchy_2 = [
    {
        "name": "Homework",
        "subtasks": [
            {
                "name": "Math assignment",
                "subtasks": [
                    {"name": "Complete worksheet"},
                    {"name": "Study for quiz"}
                ]
            },
            {
                "name": "History essay",
                "subtasks": [
                    {"name": "Research topic"},
                    {"name": "Write essay"}
                ]
            }
        ]
    },
    {
        "name": "Home project",
        "subtasks": [
            {
                "name": "Garden renovation",
                "subtasks": [
                    {"name": "Design garden layout"},
                    {"name": "Purchase plants and materials"}
                ]
            },
            {
                "name": "DIY furniture",
                "subtasks": [
                    {"name": "Select furniture design"},
                    {"name": "Buy materials"},
                    {"name": "Assemble furniture"}
                ]
            }
        ]
    }
]

# Testing the function with task_hierarchy_1
print("Task Hierarchy 1:")
list_tasks(task_hierarchy_1)
print("\nTask Hierarchy 2:")
list_tasks(task_hierarchy_2)
