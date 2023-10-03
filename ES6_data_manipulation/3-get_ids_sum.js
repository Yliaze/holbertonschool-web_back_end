export default function getStudentIdsSum(getListStudents) {
  const ReducedArray = getListStudents.reduce((sum, obj) => sum + obj.id, 0);
  return ReducedArray;
}
