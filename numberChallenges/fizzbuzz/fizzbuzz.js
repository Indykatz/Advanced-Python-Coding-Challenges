// FizzBuzz
// number / by 3 fizz
// number / by 5 buzz
// number / by 3 and 5 fizzbuzz

const Fizzbuzz = () => {
  for (number = 0; number < 101; number++) {
    if (number % 3 == 0 && number % 5 == 0) {
      console.log("Fizzbuzz");
    } else if (number % 3 == 0) {
      console.log("Fizz");
    } else if (number % 5 == 0) {
      console.log("Buzz");
    } else {
      console.log(number);
    }
  }
};

Fizzbuzz();
