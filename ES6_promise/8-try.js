function divideFunction(numerator, denominator) {
  if (denominator !== 0) {
    try {
      return (numerator / denominator);
    } catch (Error) {
      throw Error('cannot divide by 0');
    }
  }
  return (numerator / denominator);
}

export default divideFunction;
