export default function getListStudentIds(objectsArray) {
  let idsArray = [];
  if (Array.isArray(objectsArray)) {
    idsArray = objectsArray.map((obj) => obj.id);
    return idsArray;
  }
  return idsArray;
}
