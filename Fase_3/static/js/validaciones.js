function soloNumeros1(e) {
  textoArea = document.getElementById("carnet").value;
  var total = textoArea.length;
  if (total == 0) 
  {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toString();
    letras = "1234567890";

    if (letras.indexOf(tecla) == -1) 
    {
      return false;
    }
  } 
  else if (total > 0) 
  {
    if (window.event) 
    {
      keynum = e.keyCode; 
    } 
    else 
    {
      keynum = e.which;
    }
    if ((keynum >= 48 && keynum <= 57)) 
    {
      return true;
    } 
    else 
    {
      return false;
    }
  }
}

function soloNumeros2(e) {
  textoArea = document.getElementById("dpi").value;
  var total = textoArea.length;
  if (total == 0) 
  {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toString();
    letras = "1234567890";

    if (letras.indexOf(tecla) == -1) 
    {
      return false;
    }
  } 
  else if (total > 0) 
  {
    if (window.event) 
    {
      keynum = e.keyCode; 
    } 
    else 
    {
      keynum = e.which;
    }
    if ((keynum >= 48 && keynum <= 57)) 
    {
      return true;
    } 
    else 
    {
      return false;
    }
  }
}

function soloNumeros3(e) {
  textoArea = document.getElementById("edad").value;
  var total = textoArea.length;
  if (total == 0) 
  {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toString();
    letras = "1234567890";

    if (letras.indexOf(tecla) == -1) 
    {
      return false;
    }
  } 
  else if (total > 0) 
  {
    if (window.event) 
    {
      keynum = e.keyCode; 
    } 
    else 
    {
      keynum = e.which;
    }
    if ((keynum >= 48 && keynum <= 57)) 
    {
      return true;
    } 
    else 
    {
      return false;
    }
  }
}