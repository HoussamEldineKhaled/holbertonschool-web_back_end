const fs = require('fs').promises;

function readDatabase(path) {
  return fs.readFile(path, 'utf-8').then((data) => {
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const studentLines = lines.slice(1);

    const studentFields = {};

    studentLines.forEach((line) => {
      const columns = line.split(',');
      if (columns.length === 4) {
        const firstName = columns[0].trim();
        const field = columns[3].trim();

        if (!studentFields[field]) {
          studentFields[field] = [];
        }
        studentFields[field].push(firstName);
      }
    });
    return studentFields;
  })
    .catch((error) => {
      throw Error(error);
    });
}

module.exports = readDatabase;
