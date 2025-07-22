const fs = require('fs').promises;
const express = require('express');

function countStudents(path) {
  return fs.readFile(path, 'utf-8').then((data) => {
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const studentLines = lines.slice(1);

    let result = `Number of students: ${studentLines.length}\n`;

    const fieldGroups = {};

    studentLines.forEach((line) => {
      const studentData = line.split(',');

      if (studentData.length === 4) {
        const firstName = studentData[0].trim();
        const field = studentData[3].trim();

        if (!fieldGroups[field]) {
          fieldGroups[field] = [];
        }
        fieldGroups[field].push(firstName);
      }
    });

    Object.keys(fieldGroups).forEach((field) => {
      const studentList = fieldGroups[field];
      result += `Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}\n`;
    });
    return result;
  }).catch(() => {
    throw new Error('Cannot load the database');
  });
}

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const databasePath = process.argv[2];

  if (!databasePath) {
    res.status(500).send('This is the list of our students\nCannot load the database');
    return;
  }
  countStudents(databasePath).then((studentData) => {
    res.send(`This is the list of our students\n${studentData.trim()}`);
  }).catch((error) => {
    res.status(500).send(`This is the list of our students\n${error.message}`);
  });
});

app.listen(1245);

module.exports = app;
