const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, 'utf-8').then((data) => {
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const studentLines = lines.slice(1);

    console.log(`Number of students: ${studentLines.length}`);

    const fieldGroups = {};

    studentLines.forEach((line) => {
      const studentData = line.split(',');

      if (studentData.length === 4) {
        const firstName = studentData[0];
        const field = studentData[3];

        if (!fieldGroups[field]) {
          fieldGroups[field] = [];
        }
        fieldGroups[field].push(firstName);
      }
    });

    Object.keys(fieldGroups).forEach((field) => {
      const studentList = fieldGroups[field];
      console.log(`Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}`);
    });
  }).catch(() => {
    throw new Error('Cannot load the database');
  });
}

module.exports = countStudents;
