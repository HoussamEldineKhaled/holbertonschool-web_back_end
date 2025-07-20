const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const studentLines = lines.slice(1);

    console.log(`Number of students: ${studentLines.length}`);

    const fieldGroups = {};

    studentLines.forEach((line) => {
      const column = line.split(',');

      if (column.length === 4) {
        const firstName = column[0].trim();
        const field = column[3].trim();

        if (!fieldGroups[field]) {
          fieldGroups[field] = [];
        }
        fieldGroups[field].push(firstName);
      }
    });

    for (const [field, students] of Object.entries(fieldGroups)) {
      console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
    }
  } catch (e) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
