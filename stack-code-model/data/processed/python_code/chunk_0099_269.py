class XML_{

////////////////////////////////////////////////////////////////////////////////////////////////////////

public static function getAtrybut(child,atr){
	child.attributes[atr]
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

public static function getArrayObject(date_,node_name) {
	var node_name;
	delete counter
	var counter =new Array();
	var array = new Array();
	var il = date_.childNodes.length;
	for (var i = 0; i<il; i++) {
		var row = date_.childNodes[i];
		if (node_name == row.nodeName || node_name == undefined||node_name==0) {
			var g =counter.push(1)-1
			array[g] = new Object();
			for (var b in row.attributes) {
				var tt = row.attributes[b];
				array[g][b] = tt;
			}
		array[g].child = row;
	}}
	return array;
};

/////////////////////////////////////////////////////////////////////////////////////////////////////////

public static function child(target_,nod) {
for(var i=0;i<target_.childNodes.length;i++){
var row=target_.childNodes[i]

if(row.nodeName==nod){
	//trace(row.nodeName+" == "+nod)
return row
break
}}}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

}