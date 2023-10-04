export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') {
    return '';
  }

  let result = '';
  for (const value of set.values()) {
    if (value && value.startsWith(startString)) {
      result += `${value.slice(startString.length)}-`;
    }
  }

  if (result.endsWith('-')) {
    result = result.slice(0, -1);
  }

  return result;
}
