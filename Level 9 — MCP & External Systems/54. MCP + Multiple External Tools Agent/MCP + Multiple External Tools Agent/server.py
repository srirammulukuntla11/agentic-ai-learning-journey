from mcp.server.fastmcp import FastMCP
import sqlite3


mcp = FastMCP("Multiple External Tools Server")


# Tool 1 — Calculator
@mcp.tool()
def calculate_sum(a: int, b: int) -> str:
    """Add two numbers and return the result."""

    result = a + b

    return f"The sum of {a} and {b} is {result}."


# Tool 2 — Student Database
@mcp.tool()
def get_students_by_course(course: str) -> str:
    """Get all students enrolled in a specific course."""

    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, name, course FROM students WHERE course = ?",
        (course,)
    )

    students = cursor.fetchall()

    connection.close()

    if not students:
        return f"No students found in the {course} course."

    result = []

    for student in students:
        student_id, name, student_course = student

        result.append(
            f"ID: {student_id}, Name: {name}, Course: {student_course}"
        )

    return "\n".join(result)


# Tool 3 — Text Utility
@mcp.tool()
def reverse_text(text: str) -> str:
    """Reverse the given text."""

    return text[::-1]


if __name__ == "__main__":
    mcp.run()