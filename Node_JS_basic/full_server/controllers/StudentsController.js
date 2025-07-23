const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(request, response) {
    readDatabase(process.argv[2]).then((data) => {
      const responses = ['This is the list of our students\n'];

      const fields = Object.keys(data).sort(
        (a, b) => a.toLowerCase().localeCompare(b.toLowerCase()),
      );
      fields.forEach((field) => {
        const students = data[field];
        const count = students.length;
        const firstNames = students.join(', ');

        responses.push(`Number of students in ${field}: ${count} List: ${firstNames}`);
      });
      response.status(200).send(responses.join('\n'));
    }).catch(() => {
      response.status(500).send('Cannot load the database');
    });
  }

  // eslint-disable-next-line consistent-return
  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    if (!major || (major !== 'CS' && major !== 'SWE')) {
      return response.status(500)
        .send('Major parameter must be CS or SWE');
    }
    readDatabase(process.argv[2]).then((data) => {
      const students = data[major] || [];
      const firstName = students.join(', ');
      return response.status(200).send(`List: ${firstName}`);
    })
      .catch(() => response.status(500)
        .send('Cannot load the database'));
  }
}

module.exports = StudentsController;
