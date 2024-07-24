function reverse(x: number): number {
  const isNegative = x < 0 ? true : false;
  const num = isNegative ? x * -1 : x;
  const numList = String(num).split("");
  const reversedList = numList.reverse();
  const newNum = Number(reversedList.join(""));
  if (newNum > 2 ** 31 - 1) {
    return 0;
  }
  return isNegative ? newNum * -1 : newNum;
}
