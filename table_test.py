

print "Content-type: text/html"

print


print """

<html>
<head><script type="text/javascript">

function strech(obj){

var v=document.getElementById(obj.id);

l=v.innerHTML

k=l.substring(0,l.length/2)

v.innerHTML=k

v.width="100"

}



</script></head>
<body>

<table border="1">

<tr><td id="5" onclick="strech(this)">dfafffffffffffffffffffffa</td></tr>
<tr><td><input type="button" id="2" value="sads" onclick="strech(this)"></td></tr>


<tr><td></td></tr>


</table>

</body>
</html>"""
