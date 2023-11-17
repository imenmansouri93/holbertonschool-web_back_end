import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

function handleProfileSignup(firstName, lastName, fileName) {
  const promise1 = {
    status: 'pending',
  };
  const promise2 = {
    status: 'pending',
  };

  try {
    const upload = uploadPhoto(fileName);
    promise1.status = 'fulfilled';
    promise1.value = upload;
  } catch (error) {
    promise1.status = 'rejected';
    promise1.value = error.toString();
  }
  try {
    const signup = signUpUser(firstName, lastName);
    promise2.status = 'fulfilled';
    promise2.value = signup;
  } catch (error) {
    promise1.status = 'rejected';
    promise1.value = error.toString();
  }

  return [promise2, promise1];
}

export default handleProfileSignup;
