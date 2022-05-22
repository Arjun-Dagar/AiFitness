function calculate() {
  let height = document.querySelectorAll("input")[0].value;
  let weight = document.querySelectorAll("input")[1].value;
  // console.log(height);
  // console.log(weight);
  height = height / 100;
  let ans = weight / height;
  ans = ans / height;
  ans = ans.toFixed(2);
  // console.log(ans);
  if (ans <= 18.5) {
      document.getElementById("bmi-result").style.background = "#06b0fe";
      document.getElementById("bmi-result").innerText = "Your BMI is: " + ans + " (underweight)";
  }
  else if(ans > 18.5 && ans <= 24.9)
  {
    document.getElementById("bmi-result").style.background = "#87e43e";
    document.getElementById("bmi-result").innerText = "Your BMI is: " + ans + " (Normal)";
  }
  else if(ans > 24.9 && ans<= 29.9)
  {
    document.getElementById("bmi-result").style.background = "#ffca00";
    document.getElementById("bmi-result").innerText = "Your BMI is: " + ans + " (Overweight)";
  }
  else if(ans > 29.9 && ans<= 34.9){
    document.getElementById("bmi-result").style.background = "#ff8a07";
      document.getElementById("bmi-result").innerText = "Your BMI is: " + ans + " (Obese 1)";
  }
  else if(ans> 34.9 && ans<=39.9)
  {
    document.getElementById("bmi-result").style.background = "#ff5a1a";
    document.getElementById("bmi-result").innerText = "Your BMI is: " + ans + " (Obese 2)";
  }
  else
  {
    document.getElementById("bmi-result").style.background = "#f80000";
    document.getElementById("bmi-result").innerText = "Your BMI is: " + ans + " (Obese 3)";
  }
}
