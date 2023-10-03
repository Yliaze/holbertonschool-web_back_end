export default function getStudentsByLocation(getListStudents, city) {
  const locationsArray = getListStudents.filter((obj) => obj.location === city);
  return locationsArray;
}
