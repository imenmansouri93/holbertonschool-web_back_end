function divideFunction(numerator, denominator) {
  if (denominator !== 0) {
    try {
      return (numerator / denominator);
    } catch (error) {
      return error('cannot divide by 0');
    }
  }
  return (numerator / denominator);
}

export default divideFunction;
