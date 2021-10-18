function soloLetras(e) {
  textoArea = document.getElementById("usuario").value;
  var total = textoArea.length;
  if (total == 0) {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toString();
    letras = " áéíóúabcdefghijklmnñopqrstuvwxyzÁÉÍÓÚABCDEFGHIJKLMNÑOPQRSTUVWXYZ"; //Se define todo el abecedario que se quiere que se muestre.
    especiales = [8, 9, 37, 39, 46, 6]; //Es la validación del KeyCodes, que teclas recibe el campo de texto.

    tecla_especial = false
    for (var i in especiales) {
      if (key == especiales[i]) {
        tecla_especial = true;
        break;
      }
    }

    if (letras.indexOf(tecla) == -1 && !tecla_especial) {
      return false;
    }

  } else if (total > 0) {
    if (window.event) { //asignamos el valor de la tecla a keynum
      keynum = e.keyCode; //IE
    } else {
      keynum = e.which; //FF
    }
    //comprobamos si se encuentra en el rango numérico y que teclas no recibirá.
    if ((keynum > 64 && keynum < 91) || (keynum > 47 && keynum < 58) || (keynum > 96 && keynum < 132) || keynum == 8 || keynum == 13 || keynum == 6) {
      return true;
    } else {
      return false;
    }

  }

}


function validar()
{
    var a=document.getElementById("pass1").value;
    var b=document.getElementById("pass2").value;
    //alert(a+" "+b);
    var k=false;
    if(a!=b)
    {
      //alert("diferentes");
      document.getElementById('msg').style.display = 'block';
      k= false;
    }
    else
    {
      //alert("iguales");
      document.getElementById('msg').style.display = 'none';
      k= true;
    }
    return k;
}
