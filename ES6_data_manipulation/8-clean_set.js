export default function cleanSet(set, startString) {
  if (startString !== '') {
    const transformArray = Array.from(set);
    const cleanArray = transformArray.filter((obj) => obj.startsWith(startString));

    let result = '';
    for (const value of cleanArray) {
      result += `${value.slice(startString.length)}-`;
    }
    result = result.slice(0, -1);
    return result;
  }
  return '';
}
