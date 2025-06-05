function updateStudentGradeByCity(studentList, city, newGrades) {
    return studentList.filter(student => student.location === city).map(
	student => {
	    const grading = newGrades.find(grade => grade.studentId === student.id);

	    return {...student, grade: grading ? grading : 'N/A'};
	}
    );
};

export default updateStudentGradeByCity;
