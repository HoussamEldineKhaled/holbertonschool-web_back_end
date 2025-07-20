
const fs = require('fs');

function countStudents(path){
    try{
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.trim.split('\n');
    const nb = lines.length - 1;
    console.log(`Number of students: ${nb}`);
    } catch (e) {
    throw new Error('Cannot load the database');
    }
}