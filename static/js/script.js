function todayDate(){
    var d = new Date();
    var n = d.getFullYear() + "  ";
    return document.getElementById("date").innerHTML = n;
  }

todayDate()

const alert = bootstrap.Alert.getOrCreateInstance('#myAlert');
setTimeout(() => {
  alert.close()
}, 2000);
