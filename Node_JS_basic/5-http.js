const http = require('http');
const fs = require('fs').promises;

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

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');

    try {
      const databasePath = process.argv[2];
      if (!databasePath) {
        res.write('Cannot load the database');
        res.end();
        return;
      }

      const studentInfo = await countStudents(databasePath);

      res.write(studentInfo);
      res.end();
    } catch (error) {
      res.write(error.message);
      res.end();
    }
  } else {
    res.writeHead(404);
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;
