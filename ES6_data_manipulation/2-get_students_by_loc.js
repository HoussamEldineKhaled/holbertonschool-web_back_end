function getStudentsByLocation(studentList, city) {
  return studentList.filter((c) => c.location === city);
}

export default getStudentsByLocation;
