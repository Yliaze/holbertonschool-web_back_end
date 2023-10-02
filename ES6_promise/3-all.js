import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const allPromise = Promise.all([uploadPhoto(), createUser()]);
  allPromise.then((results) => {
    console.log(results[0].body, results[1].firstName, results[1].lastName);
  })
    .catch(() => {
      console.error('Signup system offline');
    });
}
