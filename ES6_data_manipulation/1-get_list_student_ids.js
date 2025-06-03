function getListStudentIds(userArr) {
  if (!Array.isArray(userArr)) {
    return [];
  }
  return userArr.map((user) => user.id);
}

export default getListStudentIds;
