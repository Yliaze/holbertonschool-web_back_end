export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const Success = true;
    if (Success) {
      resolve('Promise resolved');
    } else {
      reject(new Error('Promise rejected'));
    }
  });
}
