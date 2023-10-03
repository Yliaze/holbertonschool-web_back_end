export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  const locationsFilter = getListStudents.filter((obj) => obj.location === city);

  const gradesArray = locationsFilter.map((studentObj) => {
    const gradeFind = newGrades.find((grade) => grade.studentId === studentObj.id);
    if (gradeFind) {
      return {
        id: studentObj.id,
        firstName: studentObj.firstName,
        location: studentObj.location,
        grade: gradeFind.grade,
      };
    }
    return {
      id: studentObj.id,
      firstName: studentObj.firstName,
      location: studentObj.location,
      grade: 'N/A',
    };
  });
  return gradesArray;
}
