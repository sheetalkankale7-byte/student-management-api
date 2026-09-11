const API_URL = "http://127.0.0.1:8000";


// ====================
// ADD STUDENT
// ====================
async function addStudent() {

    const name = document.getElementById("name").value;
    const course = document.getElementById("course").value;
    const marks = document.getElementById("marks").value;

    if (name === "" || course === "" || marks === "") {
        alert("Please fill all fields");
        return;
    }

    try {

        const response = await fetch(
            `${API_URL}/students?name=${encodeURIComponent(name)}&course=${encodeURIComponent(course)}&marks=${marks}`,
            {
                method: "POST"
            }
        );

        if (!response.ok) {
            throw new Error("Failed to add student");
        }

        const data = await response.json();

        console.log("Added:", data);

        alert("Student added successfully!");

        document.getElementById("name").value = "";
        document.getElementById("course").value = "";
        document.getElementById("marks").value = "";

        // Refresh table
        getStudents();

    } catch (error) {

        console.error("Add Error:", error);
        alert("Error while adding student");

    }
}


// ====================
// GET STUDENTS
// ====================
async function getStudents() {

    try {

        const response = await fetch(`${API_URL}/students`);

        if (!response.ok) {
            throw new Error("Failed to get students");
        }

        const students = await response.json();

        console.log("Students received:", students);

        const table = document.getElementById("studentTable");

        table.innerHTML = "";

        students.forEach(student => {

            const row = `
                <tr>

                    <td>${student.id}</td>

                    <td>${student.name}</td>

                    <td>${student.course}</td>

                    <td>${student.marks}</td>

                    <td>

                        <button class="edit-btn"
                            onclick="updateStudent(${student.id})">
                            Edit
                        </button>

                        <button class="delete-btn"
                            onclick="deleteStudent(${student.id})">
                            Delete
                        </button>

                    </td>

                </tr>
            `;

            table.innerHTML += row;
        });

    } catch (error) {

        console.error("GET Error:", error);

        alert("Cannot load students");

    }
}


// ====================
// DELETE STUDENT
// ====================
async function deleteStudent(id) {

    const confirmDelete = confirm(
        "Do you want to delete this student?"
    );

    if (!confirmDelete) {
        return;
    }

    try {

        const response = await fetch(
            `${API_URL}/students/${id}`,
            {
                method: "DELETE"
            }
        );

        if (!response.ok) {
            throw new Error("Delete failed");
        }

        alert("Student deleted!");

        getStudents();

    } catch (error) {

        console.error("Delete Error:", error);

        alert("Error while deleting student");

    }
}


// ====================
// UPDATE STUDENT
// ====================
async function updateStudent(id) {

    const name = prompt("Enter new name:");
    const course = prompt("Enter new course:");
    const marks = prompt("Enter new marks:");

    if (!name || !course || !marks) {
        return;
    }

    try {

        const response = await fetch(
            `${API_URL}/students/${id}?name=${encodeURIComponent(name)}&course=${encodeURIComponent(course)}&marks=${marks}`,
            {
                method: "PUT"
            }
        );

        if (!response.ok) {
            throw new Error("Update failed");
        }

        alert("Student updated!");

        getStudents();

    } catch (error) {

        console.error("Update Error:", error);

        alert("Error while updating student");

    }
}


// ====================
// LOAD STUDENTS WHEN PAGE OPENS
// ====================
window.onload = function () {

    getStudents();

};