function v(val) {
    document.getElementById("answer").value += val;
}

function c() {
    document.getElementById("answer").value = "";
}

function getXmlHttp() {
    var xmlhttp;
    try {
        xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
    } catch (e) {
        try {
            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        } catch (E) {
            xmlhttp = false;
        }
    }
    if (!xmlhttp && typeof XMLHttpRequest != 'undefined') {
        xmlhttp = new XMLHttpRequest();
    }
    return xmlhttp;
}

function sl() {
	document.getElementById("answer").value = document.getElementById("answer").value.slice(0, -1);
}

function dp() {
	document.getElementById("answer").value += ".";
}

function raising2() {
	document.getElementById("answer").value += "^";
}

function plus_minus() {
	val = document.getElementById("answer").value;	
	if (val.charAt(0) == "-") {
  		val = val.substring(1);
	} else {
  		val = "-" + val;
	}
	document.getElementById("answer").value = val;
}

function Mplus() {
	if (document.getElementById("answer").value != "") {
  		document.getElementById("mem").value = "M";
  		document.getElementById("memory").value = document.getElementById("answer").value;
  	}
}

function Mminus() {
	if ((document.getElementById("mem").value != "") || (document.getElementById("memory").value != ""))  {
  		document.getElementById("mem").value = "";
  		document.getElementById("memory").value = "";
  	}
}

function MC() {
	if ((document.getElementById("mem").value == "M") && (document.getElementById("memory").value != ""))  {
  		document.getElementById("memory").value = "0";
  	}
}

function MR() {
	if ((document.getElementById("mem").value == "M") && (document.getElementById("memory").value != ""))  {
  		document.getElementById("answer").value = document.getElementById("memory").value;
  	}
}

function MS() {
	if (document.getElementById("answer").value != "") {
  		document.getElementById("mem").value = "M";
  		document.getElementById("memory").value = document.getElementById("answer").value;
  	}
}

function result() {
    var a = document.getElementById("answer").value;

    var xmlhttp = getXmlHttp();
    xmlhttp.open('POST', '', true);
    xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xmlhttp.send("expression=" + encodeURIComponent(a));
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4) {
            if (xmlhttp.status == 200)
                document.getElementById("answer").value = xmlhttp.responseText;
        }
    }
}