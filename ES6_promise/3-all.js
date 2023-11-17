import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((values) => {
      const { body } = values[0];
      const { firsName } = values[1];
      const { lastName } = values[2];
      console.log(`${body} ${firsName} ${lastName}`);
    })
    .catch(() => console.log('Signup system offline'));
}

export default handleProfileSignup();
