interface Student {
  firstName: string;
  lastName: string;
  age: number;
  location: string;
}

const student1: Student = {
  firstName: "Tikuochi",
  lastName: "Iheukwumere",
  age: 28,
  location: "PortHarcourt",
};

const student2: Student = {
  firstName: "Crystal",
  lastName: "Iheukwumere",
  age: 30,
  location: "Lagos",
};

type studentArray = Array<Student>;

const studentsList: studentArray = [student1, student2];

const body = document.querySelector("body");
const table = document.createElement("table");

studentsList.forEach((student) => {
  const row = document.createElement("tr");

  const firstNameCell = document.createElement("td");
  firstNameCell.textContent = student.firstName;

  const locationCell = document.createElement("td");
  locationCell.textContent = student.location;

  row.appendChild(firstNameCell);
  row.appendChild(locationCell);
  table.appendChild(row);
});

if (body) {
  body.appendChild(table);
}
