import gradio as gr
import requests


# FastAPI backend URL
BASE_URL = "http://127.0.0.1:8002"


# ============================================================
# ADD STUDENT
# ============================================================

def add_student(name, course, marks):

    response = requests.post(
        f"{BASE_URL}/students",
        params={
            "name": name,
            "course": course,
            "marks": marks
        }
    )

    return response.json()


# ============================================================
# VIEW ALL STUDENTS
# ============================================================

def view_students():

    response = requests.get(
        f"{BASE_URL}/students"
    )

    return response.json()


# ============================================================
# UPDATE STUDENT
# ============================================================

def update_student(student_id, name, course, marks):

    response = requests.put(
        f"{BASE_URL}/students/{student_id}",
        params={
            "name": name,
            "course": course,
            "marks": marks
        }
    )

    return response.json()


# ============================================================
# DELETE STUDENT
# ============================================================

def delete_student(student_id):

    response = requests.delete(
        f"{BASE_URL}/students/{student_id}"
    )

    return response.json()


# ============================================================
# GRADIO INTERFACE
# ============================================================

with gr.Blocks(title="Student Management System") as app:

    gr.Markdown("# 🎓 Student Management System")
    gr.Markdown("Manage student records using FastAPI, Supabase and Gradio.")


    # --------------------------------------------------------
    # ADD STUDENT
    # --------------------------------------------------------

    with gr.Tab("➕ Add Student"):

        name = gr.Textbox(
            label="Student Name",
            placeholder="Enter student name"
        )

        course = gr.Textbox(
            label="Course",
            placeholder="Enter course"
        )

        marks = gr.Number(
            label="Marks",
            precision=0
        )

        add_button = gr.Button("Add Student")

        add_output = gr.JSON(
            label="Response"
        )

        add_button.click(
            add_student,
            inputs=[name, course, marks],
            outputs=add_output
        )


    # --------------------------------------------------------
    # VIEW STUDENTS
    # --------------------------------------------------------

    with gr.Tab("👀 View Students"):

        view_button = gr.Button("View All Students")

        view_output = gr.JSON(
            label="Students"
        )

        view_button.click(
            view_students,
            inputs=[],
            outputs=view_output
        )


    # --------------------------------------------------------
    # UPDATE STUDENT
    # --------------------------------------------------------

    with gr.Tab("✏️ Update Student"):

        update_id = gr.Number(
            label="Student ID",
            precision=0
        )

        update_name = gr.Textbox(
            label="Student Name"
        )

        update_course = gr.Textbox(
            label="Course"
        )

        update_marks = gr.Number(
            label="Marks",
            precision=0
        )

        update_button = gr.Button("Update Student")

        update_output = gr.JSON(
            label="Response"
        )

        update_button.click(
            update_student,
            inputs=[
                update_id,
                update_name,
                update_course,
                update_marks
            ],
            outputs=update_output
        )


    # --------------------------------------------------------
    # DELETE STUDENT
    # --------------------------------------------------------

    with gr.Tab("🗑️ Delete Student"):

        delete_id = gr.Number(
            label="Student ID",
            precision=0
        )

        delete_button = gr.Button("Delete Student")

        delete_output = gr.JSON(
            label="Response"
        )

        delete_button.click(
            delete_student,
            inputs=delete_id,
            outputs=delete_output
        )


# ============================================================
# START GRADIO
# ============================================================

app.launch()