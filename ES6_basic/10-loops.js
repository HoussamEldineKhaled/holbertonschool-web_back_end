export default function appendToEachArrayValue(array, appendString) {
  const arr2 = [];
  for (const value of array) {
    arr2.push(appendString + value);
  }

  return arr2;
}
