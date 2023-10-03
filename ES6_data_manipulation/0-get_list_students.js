export default function getListStudents() {
  const objectsArray = [];
  objectsArray.push(
    { id: 1, firstName: 'Guillaume', location: 'San Francisco' },
    { id: 2, firstName: 'James', location: 'Columbia' },
    { id: 5, firstName: 'Serena', location: 'San Francisco' },
  );
  return objectsArray;
}
