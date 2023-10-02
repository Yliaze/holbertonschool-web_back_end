import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

// The one by Holberton dev :

export default function handleProfileSignup(firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName);
  const photoPromise = uploadPhoto(fileName);

  return Promise.allSettled([userPromise, photoPromise])
    .then((results) => results.map((result) => ({
      status: result.status,
      value: result.status === 'fulfilled' ? result.value : result.reason.toString(),
    })));
}

// Real One by normal dev :

// export default function handleProfileSignup(firstName, lastName, fileName) {
//   return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
//     .then((results) => {
//       console.log(results);
//     });
// }
